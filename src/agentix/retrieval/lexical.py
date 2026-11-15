"""Offline lexical scoring for arbitrary domain terms and Python identifiers."""

import math
import re
from collections import Counter

from .policy import BM25_B, BM25_IDF_SMOOTHING, BM25_K1


def tokens(text: str) -> list[str]:
    """Keep complete Unicode identifiers and add underscore/camel-case segments."""
    result = []
    for word in re.findall(r"\w+", text, flags=re.UNICODE):
        result.append(word.casefold())
        segmented = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", word)
        segmented = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", segmented).replace("_", " ")
        parts = segmented.casefold().split()
        if parts != [word.casefold()]:
            result.extend(parts)
    return result


def bm25(documents: dict[str, str], query: str) -> dict[str, float]:
    """Return positive BM25 scores using k1=1.5 and b=0.75; no persistent side index.

    Rebuild from the same stored snapshot used for semantic retrieval. This favors
    correctness after updates/reopen over large-corpus performance in the first release.
    """
    counts = {key: Counter(tokens(text)) for key, text in documents.items()}
    lengths = {key: sum(count.values()) for key, count in counts.items()}
    average = sum(lengths.values()) / max(len(counts), 1) or 1
    scores = dict.fromkeys(documents, 0.0)
    for term in sorted(set(tokens(query))):
        frequency = sum(term in count for count in counts.values())
        idf = math.log(
            1 + (len(counts) - frequency + BM25_IDF_SMOOTHING) / (frequency + BM25_IDF_SMOOTHING)
        )
        for key, count in counts.items():
            tf = count[term]
            length_normalization = 1 - BM25_B + BM25_B * lengths[key] / average
            scores[key] += idf * tf * (BM25_K1 + 1) / (tf + BM25_K1 * length_normalization)
    return {key: score for key, score in scores.items() if score > 0}
