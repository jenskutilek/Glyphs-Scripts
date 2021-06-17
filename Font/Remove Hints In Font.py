# MenuTitle: Remove Hints
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from GlyphsApp import Glyphs, TOPGHOST, STEM, BOTTOMGHOST

__doc__ = """
Remove PostScript hints in all glyphs of the current font
"""

ps_hints = [
    TOPGHOST,
    STEM,
    BOTTOMGHOST,
]

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    for layer in g.layers:
        delete = []
        for i, hint in enumerate(layer.hints):
            if hint.isPostScript and hint.type in ps_hints:
                delete.append(i)
        if delete:
            for i in reversed(delete):
                del layer.hints[i]

Glyphs.font.enableUpdateInterface()
