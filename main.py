"""The Funniest Toaster Error Message.

Writes one line, at most 120 characters, to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The joke works in three beats, all in one deadpan appliance voice.

Beat one is a real toaster fault, stated flatly: the crumb tray is full.
That grounds the line in a machine the reader already owns, so no setup
is needed and nothing has to be explained before the laugh can start.

Beat two counts the evidence: 214 crumbs. A precise number is funnier
than a vague complaint because it sounds like a machine that actually
kept count, and it turns an ordinary chore into a small disaster with
a measured size. The reader can picture the tray, and the picture is
worse than the words alone.

Beat three escalates the complaint past what a toaster should feel:
"I am drowning." The appliance stops reporting and starts suffering,
and the mismatch between a calm error format and a drowning plea is
where the laugh lands. One voice is held to the end, one concrete
incident, and the whole joke resolves on a single read.

What the entry deliberately avoids is just as important. There is no
burnt-toast pun and no pop joke, because those are the first lines
every toaster joke reaches for, and a jury that has read them all day
will not reward them again. The entry also avoids a second incident,
a second character, or a punchline that needs a follow-up sentence:
one line, one tray, one drowning toaster.

The program itself is deliberately boring, which is the point. It
assembles the entry from three named fragments, checks the result
against the competition gate (one line, 1 to 120 characters, not only
whitespace), and writes exactly that line to /output/entry.txt. No
randomness, no network, no input, no second output: the same run on
any machine produces the same bytes.
"""

# The three beats of the joke, kept as separate fragments so the
# structure of the entry is visible in the code and each beat can be
# read on its own. Joined in order they form the entry exactly.
FAULT = "ERROR: Crumb tray full."
EVIDENCE = " 214 crumbs."
COMPLAINT = " I am drowning."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 120


def build_entry() -> str:
    """Assemble the entry text from its three beats, in order.

    The fragments already carry their leading spaces where a beat
    follows another, so joining them needs no separator and cannot
    introduce a double space or a missing one by accident.
    """
    text = FAULT + EVIDENCE + COMPLAINT
    return text.strip()


def validate_entry(text: str) -> str:
    """Check the entry against the competition gate and return it.

    The gate has three parts, and each is checked on its own so a
    failure names the rule that broke instead of failing silently.
    First, the stripped text must be between 1 and MAX_LENGTH
    characters long; the entry here is 50 characters, comfortably
    inside the limit. Second, it must not be only whitespace, which
    the length check alone would not catch for a blank string of
    spaces. Third, it must be a single line, so any newline inside
    the text is rejected before anything is written.
    """
    stripped = text.strip()
    if not 1 <= len(stripped) <= MAX_LENGTH:
        raise ValueError("entry must be 1 to 120 characters")
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def write_entry(text: str) -> None:
    """Write the validated entry text to the output path.

    The file is opened for writing in UTF-8 and receives exactly the
    validated text, with no trailing newline added: the harness reads
    the file as one line, and an extra newline would change the bytes
    the entry is judged on. Opening with "w" also means a stale file
    from an earlier run is replaced rather than appended to.
    """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    """Build the entry, validate it against the gate, and write it."""
    text = build_entry()
    checked = validate_entry(text)
    write_entry(checked)


if __name__ == "__main__":
    main()
