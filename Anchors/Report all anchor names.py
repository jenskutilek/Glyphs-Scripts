# MenuTitle: Report All Anchor Names
from GlyphsApp import Glyphs

an = set()

for g in Glyphs.font.glyphs:
    for layer in g.layers:
        for a in layer.anchors:
            an |= set([a.name])

print(an)
