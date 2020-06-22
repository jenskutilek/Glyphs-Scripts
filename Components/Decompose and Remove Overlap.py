# MenuTitle: Decompose And Remove Overlap For Selection
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

for l in Glyphs.font.selectedLayers:
    l.decomposeComponents()
    l.removeOverlap()
