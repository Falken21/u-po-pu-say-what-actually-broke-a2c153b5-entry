"""Say What Actually Broke.

Most error messages are written to protect the software, not to help the
person reading them. "Something went wrong" is technically true and
completely useless: it hides the cause, dodges responsibility, and leaves
the user guessing whether their work survived.

This program takes the opposite approach. Its single line of error copy
names the real failure in plain language — a Friday-evening deploy, a file
that got eaten — then immediately answers the only question the user
actually has ("can I undo it?") before closing with a dry promise that a
human has been located and dealt with. Honest first, reassuring second,
funny because it is finally telling the truth.

Running the program writes that line, exactly as it stands, to
/output/entry.txt with no trailing newline.
"""

from pathlib import Path

# The whole entry: one error message that says what actually broke.
ERROR_LINE = (
    "Something went wrong: we pushed an update at 4:59 p.m. on a Friday "
    "and it ate your file. The undo button works. "
    "The developer has been found."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render_error() -> str:
    """Return the error line exactly as it should be shown to the user."""
    return ERROR_LINE


def write_error(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, creating parent dirs, no newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Render the error line and write it to the entry output file."""
    write_error(render_error(), OUTPUT_PATH)


if __name__ == "__main__":
    main()
