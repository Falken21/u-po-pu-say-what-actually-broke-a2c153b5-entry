"""Say What Actually Broke — an error message that tells the truth.

Most error copy lies by omission: "Something went wrong" and nothing else.
This one works because it does the opposite, in three beats:

1. It names the real failure. A Friday 4:59 p.m. deploy ate your file.
   No jargon, no "unexpected error", no passive voice hiding the culprit.
2. It keeps the user's trust. The undo button works — the one thing the
   user actually cares about (getting their file back) is confirmed in
   the same breath as the bad news.
3. It lands the joke. "The developer has been found" closes the loop:
   someone specific did this, and they have been located. Accountability
   as punchline.

Running this program writes the message to /output/entry.txt, exactly as
an honest error dialog would show it.
"""

from pathlib import Path

MESSAGE = (
    "Something went wrong: we pushed an update at 4:59 p.m. on a Friday "
    "and it ate your file. The undo button works. The developer has been found."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_message(path: Path = OUTPUT_PATH) -> Path:
    """Write the error message to *path*, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(MESSAGE, encoding="utf-8")
    return path


def main() -> None:
    write_message()


if __name__ == "__main__":
    main()
