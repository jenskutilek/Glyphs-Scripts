# MenuTitle: Decompose Background Layers For Selected Layers
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    layer.background.decomposeComponents()
