# MenuTitle: Report Global Glyph Set For All Open Files
from GlyphsApp import Glyphs

ggo = []

for f in Glyphs.fonts:
    ggo += [g.name for g in f.glyphs if g.export]

ggs = list(set(ggo))
ggt = tuple(ggo)  # It's faster to sort by a tuple
ggs.sort(key=lambda x: ggt.index(x))
print(" ".join(ggs))
