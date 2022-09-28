# MenuTitle: Export Nametable File
import codecs

from GlyphsApp import Glyphs, GetSaveFile, Message

__doc__ = "Export a .nam file that contains Unicode values and their assigned glyph names."

font = Glyphs.font

out_path = GetSaveFile(
    "Save Nametable",
    ProposedFileName=f"{font.familyName}.nam",
    filetypes=["nam"],
)

if out_path:

    header = f"%%FONTLAB NAMETABLE: {font.familyName}\n"

    mappings = {}
    for g in font.glyphs:
        if g.unicodes is None:
            continue
        for u in g.unicodes:
            key = f"0x{u}"
            if key not in mappings:
                mappings[key] = g.name
            else:
                Message(f"Found duplicate Unicode mapping: {key} in {g.name} and {mappings[key]}, please fix.")

    with codecs.open(out_path, "wb", "utf-8") as f:
        f.write(header)
        for k, v in sorted(mappings.items()):
            f.write(f"{k} {v}\n")
