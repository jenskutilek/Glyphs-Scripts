# MenuTitle: Decompose Background Layers For Selection
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    for g in layer.parent.parent.glyphs:
        for glyph_layer in g.layers:
            glyph_layer.background.decomposeComponents()
