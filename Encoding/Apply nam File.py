# MenuTitle: Apply Nametable File
import codecs

from GlyphsApp import Glyphs, GetOpenFile, Message, GSFont

__doc__ = "Import a .nam file that contains Unicode values and their assigned glyph names, and apply it to the current font. Glyphs in the font that are not in the nametable file have their Unicode values removed."

def clear_unicodes(font: GSFont) -> None:
    font.disableUpdateInterface()
    for g in font.glyphs:
        if g.unicodes:
            g.unicodes = None
    font.enableUpdateInterface()


nam_path = GetOpenFile(
    "Apply Nametable",
    allowsMultipleSelection=False,
    filetypes=["nam"],
    # path=
)

font = Glyphs.font

if nam_path:
    mappings = {}
    with codecs.open(nam_path, "rb", "utf-8") as f:
        lines = f.readlines()
    if len(lines) == 0:
        Message("The file is too short.")
    else:
        if not lines[0].startswith(r"%%FONTLAB NAMETABLE:"):
            Message("The file is missing the nametable header. Does it have the correct type?")
        else:
            i = 0
            for line in lines:
                if line.startswith("%"):
                    continue
                u_g = line.strip().split()
                if len(u_g) != 2:
                    Message(f"Malformed line {i}, quitting.")
                    mappings = {}
                    break
                uni, name = u_g
                if not uni.startswith("0x"):
                    Message(f"Malformed line {i}, quitting.")
                    mappings = {}
                    break
                if name in font.glyphs:
                    if name in mappings:
                        mappings[name].append(uni[2:])
                    else:
                        mappings[name] = [uni[2:]]
                i += 1
    if not mappings:
        Message(f"No Unicode mappings could be found, font is unchanged.")
    else:
        font.disableUpdateInterface()
        for g in font.glyphs:
            if g.name in mappings:
                uni = mappings[g.name]
                if g.unicodes is None or set(g.unicodes) != set(uni):
                    g.unicodes = sorted(uni)
            else:
                if g.unicodes:
                    g.unicodes = None
        font.enableUpdateInterface()
        unicodes = []
        for g in font.glyphs:
            if g.unicodes:
                unicodes.extend(g.unicodes)
            if len(unicodes) != len(set(unicodes)):
                Message("The font now contains duplicate Unicode values, please check")