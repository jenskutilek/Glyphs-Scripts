# MenuTitle: Rename Kerning Groups to Nice Names
from GlyphsApp import Glyphs


Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    lk = g.leftKerningGroup
    if lk:
        nice = Glyphs.niceGlyphName(lk)
        if nice != lk:
            print(f"{g.name} (L): {lk} -> {nice}")
            g.leftKerningGroup = nice

    rk = g.rightKerningGroup
    if rk:
        nice = Glyphs.niceGlyphName(rk)
        if nice != rk:
            print(f"{g.name} (R): {rk} -> {nice}")
            g.rightKerningGroup = nice

Glyphs.font.enableUpdateInterface()
