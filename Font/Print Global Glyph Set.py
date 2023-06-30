# MenuTitle: Report Global Glyph Set For All Open Files
from GlyphsApp import Glyphs

ggo = []

for f in Glyphs.fonts:
	ggo += [g.name for g in f.glyphs if g.export]

ggo = list(set(ggo))
print(" ".join(ggo))
