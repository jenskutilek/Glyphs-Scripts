# MenuTitle: Remove All Kerning Groups
from GlyphsApp import Glyphs


Glyphs.font.disableUpdateInterface()
for g in Glyphs.font.glyphs:
    g.leftKerningGroup = None
    g.rightKerningGroup = None
Glyphs.font.enableUpdateInterface()
