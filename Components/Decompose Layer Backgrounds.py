# MenuTitle: Decompose Background Layers For Selection
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    layer.background.decomposeComponents()
