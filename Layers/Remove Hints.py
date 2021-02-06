# MenuTitle: Remove Hints
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from GlyphsApp import Glyphs

__doc__ = """
Remove hints in selected layers. Dangerous: Also removes any corner or cap
components.
"""

Glyphs.font.disableUpdateInterface()

for layer in Glyphs.font.selectedLayers:
    layer.hints = []

Glyphs.font.enableUpdateInterface()
