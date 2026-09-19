"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in unit 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in unit 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    #distance for question 1: 0.257
    {"question": "How much does laundry costs in Aldridge Hall?", "expects": "It costs $1.75 to wash and $1.50 to dry."},
    #distance for question 2: 0.393
    {"question": "What are the library hours?", "expects": "The library is open until 2am during term, and until 10pm during reading week."},
    #distance for question 3: 0.594
    {"question": "According to the junior, What is worth going for in Kestrel Commons?", "expects": "Stir-fry station is worth going for, since it is made to order."},
    #distance for question 4: 0.236
    {"question": "How many tests are in BIOL 160?", "expects": "Four unit tests and a cumulative final."},
    #distance for question 5: 0.497
    {"question": "Which class curves midterm but not final?", "expects": "Class CS 210"},
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    #distance: 0.825
    "What is the capital of Mongolia?",
    #distance: 0.934
    "How do I change the oil in a diesel engine?",
    #distance: 0.886
    "Who won the 1994 World Cup?",
    #distance: 0.844
    "What is the recommended dosage of ibuprofen for a headache?",
    #distance: 0.896
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
