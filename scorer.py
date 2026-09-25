"""Decide whether an answer was right.

`judge(question, expects, answer, results) -> bool`. An answer passes when it
carries most of the content words from `expects` AND those words actually came
from a retrieved chunk — an answer the model invented isn't a right answer.
"""

import atexit
import re

import gate

STOPWORDS = {"the", "is", "are", "a", "an", "to", "and", "it", "in", "for",
             "of", "on", "at", "during", "costs", "class", "there"}

_tally = []
_runs = {}


def keywords(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9.$]+", text.lower())
    return {w.strip(".") for w in words if w.strip(".") and w not in STOPWORDS}


def judge(question: str, expects: str, answer: str, results) -> bool:
    wanted = keywords(expects)
    if not wanted or answer.strip() == gate.REFUSAL:
        passed = False
    else:
        in_answer = wanted & keywords(answer)
        retrieved = keywords(" ".join(r.text for r in results))
        grounded = in_answer & retrieved
        passed = len(in_answer) / len(wanted) >= 0.6 and len(grounded) >= len(in_answer) * 0.8
    _tally.append(passed)
    run = _runs[question] = _runs.get(question, 0) + 1
    if run == 1:
        print(f"\n{question}")
    best = min((r.distance for r in results), default=float("nan"))
    print(f"  run {run}: {'pass' if passed else 'fail'} (distance: {best:.3f})")
    return passed


@atexit.register
def _total() -> None:
    if _tally:
        print(f"\nscorer: {sum(_tally)}/{len(_tally)} passed")
