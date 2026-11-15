"""Trusted standard-library-only example tools staged as bytes into AppContainer.

These authored examples are maintained application fixtures, not generated artifacts.
The host validates all inputs/outputs; these annotations also document each contract.
"""

from typing import Annotated


def normalize_text(
    text: Annotated[str, "Text up to 16000 characters"],
) -> Annotated[str, "Whitespace-normalized text"]:
    """Collapse whitespace and strip leading/trailing whitespace; preserve letters."""
    return " ".join(text.split())


def count_words(
    text: Annotated[str, "Text up to 16000 characters"],
) -> Annotated[int, "Nonnegative whitespace-delimited word count"]:
    """Count nonempty whitespace-separated words; empty input returns zero."""
    return len(text.split())


def count_vowels(
    text: Annotated[str, "Text up to 16000 characters"],
) -> Annotated[int, "Nonnegative ASCII vowel count"]:
    """Count ASCII vowels case-insensitively without accent normalization."""
    return sum(character in "aeiouAEIOU" for character in text)


def summarize(
    words: Annotated[int, "Nonnegative word count"],
    vowels: Annotated[int | None, "Optional nonnegative vowel count"] = None,
) -> Annotated[dict, "Structured counts; absent vowels remain null"]:
    """Combine counts without inventing an uncomputed vowel result."""
    return {"words": words, "vowels": vowels}
