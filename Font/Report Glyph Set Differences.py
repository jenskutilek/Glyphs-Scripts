# MenuTitle: Report Glyph Set Differences

from GlyphsApp import Glyphs

reference = Glyphs.font
ref_glyphs = [g.name for g in reference.glyphs]
ref_glyphs_set = set(ref_glyphs)

for font in Glyphs.fonts:
    if font == reference:
        continue
    print(font.filepath)
    glyphs = [g.name for g in font.glyphs]
    for g in glyphs:
        if g not in ref_glyphs_set:
            print(f"    Extra: {g}")
    glyphs = set(glyphs)
    for g in ref_glyphs:
        if g not in glyphs:
            print(f"    Missing: {g}")
