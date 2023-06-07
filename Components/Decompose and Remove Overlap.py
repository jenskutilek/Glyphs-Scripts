# MenuTitle: Decompose And Remove Overlap For Selection
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    layer.decomposeComponents()
    layer.removeOverlap()
