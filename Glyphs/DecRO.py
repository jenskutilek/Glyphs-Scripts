# MenuTitle: Copy to Background, Decompose, Remove Overlaps, Correct Path Direction
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    g = layer.parent
    for layer in g.layers:
        layer.background = layer.copy()
        layer.decomposeComponents()
        layer.removeOverlap()
        layer.correctPathDirection()
