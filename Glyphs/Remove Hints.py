# MenuTitle: Remove Hints
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

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

for l in Glyphs.font.selectedLayers:
    g = l.parent
    for layer in g.layers:
        delete = []
        for i, hint in enumerate(layer.hints):
            if hint.isPostScript and hint.type in ps_hints:
                delete.append(i)
        if delete:
            for i in reversed(delete):
                del layer.hints[i]

Glyphs.font.enableUpdateInterface()
