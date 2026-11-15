"""Observe structural IDs with a trusted fixture, not model code or native evidence."""

import json
import os
import socket
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path
from urllib.request import ProxyHandler, build_opener

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
with socket.socket() as listener:
    listener.bind(("127.0.0.1", 0))
    port = listener.getsockname()[1]
with (root / "docs/reports/v4-group-probe.log").open("w") as log:
    process = subprocess.Popen(
        [sys.executable, str(root / "tests/group_id_probe.py"), str(port)], stdout=log, stderr=log
    )
    try:
        url = f"http://127.0.0.1:{port}"
        opener = build_opener(ProxyHandler({}))
        for _ in range(100):
            try:
                with opener.open(url, timeout=1):
                    break
            except Exception:
                time.sleep(0.1)
        with sync_playwright() as driver:
            browser = driver.chromium.launch(
                executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE") or None
            )
            page = browser.new_page()
            page.goto(url)
            from playwright.sync_api import expect

            for text in ("Hello World!", "AEIOUaeiou", "rhythms", "", "Hello World!", "x" * 16001):
                for name in ("words", "vowels", "words_2"):
                    page.locator("#application_" + name + "_input textarea").fill(text)
                    page.locator("#application_" + name + "_execute").click()
                    expected = "" if len(text) > 16000 else str(len(text.split()))
                    expect(page.locator("#application_" + name + "_output input")).to_have_value(
                        expected
                    )
            elements = page.locator("[id]").evaluate_all(
                "items => items.map(el => ({id: el.id, tag: el.tagName, html: el.outerHTML.slice(0,400)}))"
            )
            counts = Counter(item["id"] for item in elements)
            duplicates = {key: value for key, value in counts.items() if value > 1}
            result = {
                "duplicates": duplicates,
                "elements": [item for item in elements if item["id"] in duplicates],
            }
            (root / "docs/reports/v4-group-id-probe.json").write_text(
                json.dumps(result, indent=2), encoding="utf-8"
            )
            print(json.dumps(result, indent=2))
            browser.close()
    finally:
        process.terminate()
        process.wait(timeout=10)
