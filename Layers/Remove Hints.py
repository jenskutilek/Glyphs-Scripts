# MenuTitle: Remove Hints
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Remove hints in selected layers
"""

Glyphs.font.disableUpdateInterface()

for l in Glyphs.font.selectedLayers:
    l.hints = []

Glyphs.font.enableUpdateInterface()
