"""Scoped widget styles are gated by their closed grammar, not by the app grant."""

import hashlib
import json
import os
from types import SimpleNamespace

import pytest

STYLE = ':where([id^="application_count_words_in_text_"]) { border-radius: 12px; }'
MEMBER = "count_words_in_text_widget.css"


def test_style_bytes_never_change_the_application_identity():
    """Only executable members bind the identity; a colour edit is not a new app."""
    from agentix.lab.application_artifacts import _identity

    base = (("app.py", b"print(1)"), (MEMBER, b"a{}"))
    assert _identity(base) == _identity((("app.py", b"print(1)"), (MEMBER, b"b{}")))
    assert _identity(base) != _identity((("app.py", b"print(2)"), (MEMBER, b"a{}")))


def test_saved_style_keeps_the_approved_application_valid(tmp_path):
    """A persisted stylesheet leaves the reviewed digest and its approval usable."""
    from schema3_package import package

    from agentix.application.style_member import write_style_member
    from agentix.lab.application_artifacts import application_digest, approve_application

    folder = package(tmp_path)
    before = application_digest(folder)
    write_style_member(folder, MEMBER, STYLE)
    assert application_digest(folder) == before
    assert approve_application(folder, before).digest == before


def test_saved_style_rebinds_the_manifest_member_hash(tmp_path):
    """Capture still proves the stylesheet on disk is the one the package declares."""
    from schema3_package import package

    from agentix.application.general_package import capture
    from agentix.application.style_member import write_style_member

    folder = package(tmp_path)
    write_style_member(folder, MEMBER, STYLE)
    files = dict(capture(folder))
    assert files[MEMBER] == STYLE.encode()
    manifest = json.loads(files["application.json"])
    assert manifest["files"][MEMBER] == hashlib.sha256(STYLE.encode()).hexdigest()


def test_unsafe_style_is_rejected_and_the_file_is_unchanged(tmp_path):
    """The grammar, not human review, is what stops a style from moving controls."""
    from schema3_package import package

    from agentix.application.style_member import write_style_member

    folder = package(tmp_path)
    before = (folder / MEMBER).read_bytes()
    with pytest.raises(ValueError):
        write_style_member(
            folder,
            MEMBER,
            ':where([id^="application_count_words_in_text_"]) { position: fixed; }',
        )
    assert (folder / MEMBER).read_bytes() == before


def test_style_member_rejects_a_linked_file(tmp_path):
    """A hard link must not redirect a style write into an unrelated file."""
    from schema3_package import package

    from agentix.application.style_member import write_style_member

    folder = package(tmp_path)
    outside = tmp_path / "outside.css"
    outside.write_text("preserve outside bytes", encoding="utf-8")
    (folder / MEMBER).unlink()
    os.link(outside, folder / MEMBER)
    with pytest.raises(ValueError):
        write_style_member(folder, MEMBER, STYLE)
    assert outside.read_text(encoding="utf-8") == "preserve outside bytes"


def test_review_style_save_keeps_the_candidate_approved(tmp_path):
    """Each saved widget CSS reaches its own file without revoking approval."""
    from schema3_package import build

    from agentix.application.app_review import ApplicationReview

    candidate = build(tmp_path)
    candidate.approved = True
    identity = candidate.identity
    assert ApplicationReview().save(candidate, MEMBER, STYLE, identity) is False
    vowels_member = "count_vowels_in_text_widget.css"
    vowels_style = ':where([id^="application_count_vowels_in_text_"]) { border-radius: 31px; }'
    assert ApplicationReview().save(candidate, vowels_member, vowels_style, identity) is False
    assert candidate.approved is True
    assert candidate.identity == identity
    assert (candidate.package / MEMBER).read_text(encoding="utf-8") == STYLE
    assert (candidate.package / vowels_member).read_text(encoding="utf-8") == vowels_style


def test_review_code_save_still_revokes(tmp_path):
    """Executable edits keep the existing revoke-before-write guarantee."""
    from schema3_package import CONNECTION_CODE, build

    from agentix.application.app_review import ApplicationReview

    candidate = build(tmp_path)
    candidate.approved = True
    revoked = ApplicationReview().save(
        candidate,
        "application_logic.py",
        CONNECTION_CODE + "\n# reviewed edit\n",
        candidate.identity,
    )
    assert revoked is True
    assert candidate.approved is False


def test_installed_style_write_changes_the_installed_package(tmp_path):
    """A style save must reach the installed package, not only a disposable draft."""
    from test_code_application import make_code_candidate
    from test_widget_reuse import Protector

    from agentix.application.app_workflow import ApplicationSupervisor
    from agentix.storage.installed_apps import InstalledApps

    item = make_code_candidate(tmp_path / "authored")
    item.display_name = "Installed style application"
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    library = InstalledApps(tmp_path / "apps", tmp_path / "records", protector=Protector())
    app = library.publish(item)
    member = app.package / "calculator_widget.css"
    before = member.read_text(encoding="utf-8")
    library.write_style_member(
        app.id,
        "calculator_widget.css",
        ':where([id^="application_calculator_"]) { border-radius: 12px; }',
    )
    assert member.read_text(encoding="utf-8") != before
    assert "border-radius: 12px" in member.read_text(encoding="utf-8")
    assert library.get(app.id).digest == app.digest


def test_installed_style_write_rejects_an_unsafe_declaration(tmp_path):
    """The installed package keeps its bytes when the grammar refuses the style."""
    from test_code_application import make_code_candidate
    from test_widget_reuse import Protector

    from agentix.application.app_workflow import ApplicationSupervisor
    from agentix.storage.installed_apps import InstalledApps

    item = make_code_candidate(tmp_path / "authored")
    item.display_name = "Installed style application"
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    library = InstalledApps(tmp_path / "apps", tmp_path / "records", protector=Protector())
    app = library.publish(item)
    member = app.package / "calculator_widget.css"
    before = member.read_bytes()
    with pytest.raises(ValueError):
        library.write_style_member(
            app.id,
            "calculator_widget.css",
            ':where([id^="application_calculator_"]) { position: fixed; }',
        )
    assert member.read_bytes() == before


def test_save_file_writes_the_installed_package_for_a_style_member(tmp_path):
    """The controller forwards a style save to the installed library, not only the draft."""
    from threading import RLock

    from schema3_package import build

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.controllers.sessions import SessionRegistry

    class Library:
        def __init__(self) -> None:
            self.written = []

        def write_style_member(self, identity, name, css):
            """Record the installed write instead of touching a real library."""
            self.written.append((identity, name, css))
            return "digest"

    library = Library()
    sessions = SessionRegistry(
        lambda identity: SimpleNamespace(
            _lock=RLock(),
            state=SimpleNamespace(
                is_running=False, application_busy=False, application_review_pending=False
            ),
        )
    )
    owner = sessions.resolve(None, "alice")
    backend = ApplicationsBackend(sessions, library_factory=lambda: library)
    _, state = backend._resolve(owner.token, SimpleNamespace(session_hash="alice"))
    candidate = build(tmp_path)
    candidate.catalog_id = "c8ac00d8fd88433182572a6f404b9a7d"
    state.candidate = candidate
    message, *_ = backend.save_file(
        "count_words_in_text_widget.css",
        ':where([id^="application_count_words_in_text_"]) { border-radius: 12px; }',
        candidate.identity,
        owner.token,
        SimpleNamespace(session_hash="alice"),
    )
    assert library.written == [
        (
            "c8ac00d8fd88433182572a6f404b9a7d",
            "count_words_in_text_widget.css",
            ':where([id^="application_count_words_in_text_"]) { border-radius: 12px; }',
        )
    ]
    assert "installed application" in message


def test_served_style_wins_the_preview_cascade_and_reaches_form_controls():
    """The served copy outranks the preview sheet and styles the inner control."""
    from agentix.lab.application_session import served_style

    css = (
        b':where([id^="application_calculator_"]) { border-radius: 22px; '
        b"background-color: #26177d; font-family: Georgia; font-size: 28px; }"
    )
    served = served_style(css, "calculator", "multiplier").decode()
    assert '[id^="application_multiplier_"][id][id][id][id][id]' in served
    assert "border-radius: 22px !important" in served
    assert "font-family: Georgia !important" in served
    assert "input" in served and "font-size: 28px !important" in served
    assert ":where(" not in served
    assert "!important" not in css.decode()


def test_served_style_reaches_the_caption_span_and_spares_layout_grips():
    """The caption span is targeted directly and grips keep their own glyph size."""
    from agentix.lab.application_session import served_style

    css = (
        b':where([id^="application_calculator_"]) { font-family: Georgia; font-size: 28px; }\n'
        b':where([id^="application_calculator_"]) label { font-family: Tahoma; font-size: 27px; }'
    )
    served = served_style(css, "calculator", "multiplier").decode()
    assert "label span { font-family: Tahoma !important; font-size: 27px !important; }" in served
    assert "label label span" not in served
    assert "button:not(.application-layout-handle)" in served
    assert "input:not(.application-visibility-toggle)" in served


def test_restage_styles_rewrites_the_served_stylesheet(tmp_path):
    """A saved style reaches the file served to a reload and to the web tab."""
    from schema3_package import package

    from agentix.application.general_package import capture
    from agentix.lab.application_session import ApplicationSession

    folder = package(tmp_path)
    files = capture(folder)
    manifest = json.loads(dict(files)["application.json"])
    root = tmp_path / "staged"
    root.mkdir()
    (root / "application.css").write_bytes(b"/* base */")
    session = object.__new__(ApplicationSession)
    session.root = root
    session.application = SimpleNamespace(files=files)
    session.manifest = manifest
    session.restage_styles(
        "count_words_in_text_widget.css",
        ':where([id^="application_count_words_in_text_"]) { border-radius: 22px; }',
    )
    served = (root / "application.css").read_text(encoding="utf-8")
    assert "border-radius: 22px !important" in served
    assert "application_count_words_in_text_" in served


def test_restage_styles_preserves_successive_widget_saves(tmp_path):
    """The web sheet retains every widget's latest CSS across separate saves."""
    from schema3_package import package

    from agentix.application.general_package import capture
    from agentix.lab.application_session import ApplicationSession

    files = capture(package(tmp_path))
    manifest = json.loads(dict(files)["application.json"])
    root = tmp_path / "staged"
    root.mkdir()
    (root / "application.css").write_bytes(b"/* base */")
    session = object.__new__(ApplicationSession)
    session.root = root
    session.application = SimpleNamespace(files=files)
    session.manifest = manifest
    session.restage_styles(
        "count_words_in_text_widget.css",
        ':where([id^="application_count_words_in_text_"]) { border-radius: 22px; }',
    )
    session.restage_styles(
        "count_vowels_in_text_widget.css",
        ':where([id^="application_count_vowels_in_text_"]) { border-radius: 31px; }',
    )
    served = (root / "application.css").read_text(encoding="utf-8")
    assert "border-radius: 22px !important" in served
    assert "border-radius: 31px !important" in served


def test_restage_styles_keeps_the_base_stylesheet(tmp_path):
    """Rebuilding the served sheet must not drop the base UI stylesheet."""
    from schema3_package import package

    from agentix.application.general_package import capture
    from agentix.lab.application_session import STYLE_MARKER, ApplicationSession

    folder = package(tmp_path)
    files = capture(folder)
    manifest = json.loads(dict(files)["application.json"])
    root = tmp_path / "staged"
    root.mkdir()
    base = b"/* base */\n.gradio-container { color: #fff; }"
    (root / "application.css").write_bytes(base + b"\n" + STYLE_MARKER + b"\nold")
    session = object.__new__(ApplicationSession)
    session.root = root
    session.application = SimpleNamespace(files=files)
    session.manifest = manifest
    session.restage_styles(
        "count_words_in_text_widget.css",
        ':where([id^="application_count_words_in_text_"]) { border-radius: 22px; }',
    )
    served = (root / "application.css").read_bytes()
    assert served.startswith(base)
    assert served.count(STYLE_MARKER) == 1
    assert b"border-radius: 22px !important" in served
    assert b"old" not in served


def test_record_sealed_with_the_legacy_digest_still_loads(tmp_path):
    """An application installed before the identity change is not reported as tampered."""
    import json

    from test_code_application import make_code_candidate
    from test_widget_reuse import Protector

    from agentix.application.app_workflow import ApplicationSupervisor
    from agentix.lab.application_artifacts import application_digest
    from agentix.storage.installed_apps import InstalledApps, _legacy_digest

    item = make_code_candidate(tmp_path / "authored")
    item.display_name = "Legacy digest application"
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    library = InstalledApps(tmp_path / "apps", tmp_path / "records", protector=Protector())
    installed = library.publish(item)
    assert _legacy_digest(installed.package) != application_digest(installed.package)
    record_path = library._record(installed.id)
    record = json.loads(Protector().unseal(record_path.read_bytes()))
    record["digest"] = _legacy_digest(installed.package)
    record_path.write_bytes(Protector().seal(json.dumps(record).encode()))
    assert library.get(installed.id).digest == record["digest"]


def test_legacy_digest_does_not_accept_a_changed_member(tmp_path):
    """The compatibility comparison still refuses an edited executable member."""
    import json

    from test_code_application import make_code_candidate
    from test_widget_reuse import Protector

    from agentix.application.app_workflow import ApplicationSupervisor
    from agentix.storage.installed_apps import InstalledApps, _legacy_digest

    item = make_code_candidate(tmp_path / "authored")
    item.display_name = "Legacy digest application"
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    library = InstalledApps(tmp_path / "apps", tmp_path / "records", protector=Protector())
    installed = library.publish(item)
    record_path = library._record(installed.id)
    record = json.loads(Protector().unseal(record_path.read_bytes()))
    record["digest"] = _legacy_digest(installed.package)
    record_path.write_bytes(Protector().seal(json.dumps(record).encode()))
    (installed.package / "application_logic.py").write_text("# edited\n", encoding="utf-8")
    with pytest.raises(ValueError):
        library.get(installed.id)
