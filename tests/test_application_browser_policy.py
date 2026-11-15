"""Host browser egress policy for generated native application verification."""

import pytest


@pytest.mark.parametrize(
    "url,allowed",
    [
        ("http://127.0.0.1:45678/config", True),
        ("http://127.0.0.1:45678/assets/app.js", True),
        ("http://127.0.0.1:45679/", False),
        ("https://example.com/", False),
        ("file:///C:/private.txt", False),
        ("http://127.0.0.1:45678.evil.example/", False),
        ("http://user@127.0.0.1:45678/", False),
    ],
)
def test_browser_requests_stay_on_the_owned_origin(url, allowed):
    """Catch navigation/request escape from the supervisor's reviewed application origin."""
    from agentix.application.app_workflow import browser_origin_allowed

    assert browser_origin_allowed(url, "http://127.0.0.1:45678/") is allowed
