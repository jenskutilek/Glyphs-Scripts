# MenuTitle: Copy Glyph Mark Colors to All Fonts
from GlyphsApp import Glyphs


cf = Glyphs.font

for g in cf.glyphs:
    c = g.color
    for f in Glyphs.fonts:
        if f != cf:
            if g.name in f.glyphs:
                if f.glyphs[g.name].color != c:
                    f.glyphs[g.name].color = c
