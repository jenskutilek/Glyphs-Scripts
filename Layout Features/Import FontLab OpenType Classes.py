# MenuTitle: Import FontLab OpenType Classes
from __future__ import annotations
import codecs

from GlyphsApp import Glyphs, GetOpenFile, Message, GSClass, GSFont
from pathlib import Path
from typing import List

__doc__ = """
Import a .flc file that contains class definitions exported from FontLab Studio 5.
Unlike import from a UFO, this will preserve the sort order of the classes. Kerning
classes are ignored.
"""


class FLClass:
    def __init__(self, name: str) -> None:
        self.name = name
        self.glyphs: List[str] = []

    def to_glyphs(self, font: GSFont) -> None:
        gc = GSClass(self.name, "\n".join(self.glyphs))
        gc.active = True
        gc.automatic = False
        font.classes.append(gc)


def import_flc_file(flc_path: Path, font: GSFont):
    with codecs.open(str(flc_path), "rb", "utf-8") as f:
        lines = f.readlines()
    if len(lines) == 0:
        Message("The file is too short.")
    else:
        if not lines[0].startswith(r"%%FONTLAB CLASSES"):
            Message(
                "The file is missing the class file header. Does it have the "
                "correct type?"
            )
        else:
            i = 0
            classes: List[FLClass] = []
            cur = None
            for line in lines:
                if line.startswith("%%CLASS"):
                    parts = line.split(" ", 1)
                    if len(parts) != 2:
                        Message(f"Malformed line #{i}, aborting import: '{line}'")
                        return
                    _, name = parts
                    cur = FLClass(name.strip())

                elif line.startswith("%%GLYPHS"):
                    if cur is None:
                        Message(
                            f"No current class while parsing line #{i}, aborting import"
                        )
                        return

                    if not cur.name.startswith("_"):
                        # Only process non-kerning classes
                        parts = line.split(" ")
                        if len(parts) < 2:
                            Message(f"Malformed line #{i}, aborting import: '{line}'")
                            return
                        glyphs = [n.strip("'").strip() for n in parts[1:]]
                        cur.glyphs = glyphs

                elif line.startswith("%%END"):
                    if cur is None:
                        Message(f"Stray end marker found in line #{i}, aborting import")
                        return

                    if not cur.name.startswith("_"):
                        # Only process non-kerning classes
                        classes.append(cur)
                    cur = None

                elif line.startswith("%%KERNING"):
                    # Ignore kerning flags
                    pass

                elif line.strip() == "":
                    pass

                else:
                    print(f"Unknown line type in line #{i}: {line}")
                i += 1

            if not classes:
                Message("No classes could be imported.")

            font.disableUpdateInterface()
            font.classes = []
            for c in classes:
                c.to_glyphs(font)
            font.enableUpdateInterface()


def main():
    font = Glyphs.font
    if font is None:
        Message("Please open a glyphs file first.")
        return

    flc_path = GetOpenFile(
        "Import FontLab Classes",
        allowsMultipleSelection=False,
        filetypes=["flc"],
        # path=
    )

    if flc_path:
        import_flc_file(Path(flc_path), font)


if __name__ == "__main__":
    main()
