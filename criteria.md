# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I set the target to 4 out of 5 becuase four of the questions can be answered with retrieval. However, the fifth question requires retriving information from all classes in campus_life to calculate how many classes curve. 

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
In a Retrieval-Augumented Geneartion system, the answers or data will be retrieved from the available documents instead of generating fake answers. Ensuring the system name a source document allows the users and developer to know that the answer is in fact retrieved instead of created.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
It is unrealistic to expect the answers retrieved to be 100% right all the time. However, the RAG should still be right the majority of the time. Considering that the system is a RAG system, when the model is unable to retrieve the correct answer, instead of generating a false answer, it needs to reply "I do not have enough information about that".

---

## 4. Something about your chunks
For all generated chunks, no chunk will be under 179 characters and over 550 characters.


**Why this target:**
The selected corpora is campus_life. To retain enough content information and heading, 1 chunk should equal to 1 document. All the documents in the campus_life file is between 179 and 550 characters.



---

## 5. Speed

The response time for the RAG system should be under 5 seconds for at least 4 out of 5 questions.


**Why this target:**
The 5 second limit was selected to ensure that the RAG system remain fast for users. 4 out of 5 questions was set for the delays when calling the model, rather than requiring the response under 5 seconds 100% of the time.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
