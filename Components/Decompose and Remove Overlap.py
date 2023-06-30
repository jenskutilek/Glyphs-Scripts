# MenuTitle: Decompose And Remove Overlap For Selected Layers
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    layer.decomposeComponents()
    layer.removeOverlap()
