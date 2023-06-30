# MenuTitle: Decompose Selected Layers
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    layer.decomposeComponents()
