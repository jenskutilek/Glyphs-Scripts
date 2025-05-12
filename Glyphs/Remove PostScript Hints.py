# MenuTitle: Remove PostScript Hints
from GlyphsApp import Glyphs, TOPGHOST, STEM, BOTTOMGHOST

__doc__ = """
Remove PostScript hints in selected glyphs
"""

ps_hints = [
    TOPGHOST,
    STEM,
    BOTTOMGHOST,
]

Glyphs.font.disableUpdateInterface()

for layer in Glyphs.font.selectedLayers:
    g = layer.parent
    for layer in g.layers:
        for hint in list(layer.hints):
            if hint.isPostScript and hint.type in ps_hints:
                layer.hints.remove(hint)

Glyphs.font.enableUpdateInterface()
