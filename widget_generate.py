"""Generate a review candidate with the local application Widget Designer."""

import argparse
from pathlib import Path

import _agentix_path  # noqa: F401
from agentix.lab.widget_designer import generate_widget

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    print("Candidate review digest:", generate_widget(args.folder))
