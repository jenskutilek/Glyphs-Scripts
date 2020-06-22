# MenuTitle: Remove Hints
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Remove hints in all glyphs of the current font
"""

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    for gl in g.layers:
        gl.hints = []

Glyphs.font.enableUpdateInterface()
