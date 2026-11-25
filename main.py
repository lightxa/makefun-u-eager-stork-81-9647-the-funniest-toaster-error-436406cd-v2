"""The Funniest Toaster Error Message.

Writes one line, at most 120 characters, to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The joke: a deadpan appliance drowning in its own crumb tray. The first
beat is a real toaster fault (crumb tray full), the second beat counts the
evidence (214 crumbs), and the last beat escalates to a drowning complaint.
One voice held to the end, one concrete incident, and it lands on a single
read. No burnt-toast pun, no pop joke, nothing the obvious lines say.
"""

ENTRY = "ERROR: Crumb tray full. 214 crumbs. I am drowning."


def main() -> None:
    """Write the entry text to /output/entry.txt, exactly one line."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, "entry must be 1 to 120 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
