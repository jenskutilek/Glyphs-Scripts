# MenuTitle: Decompose Selection
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

for layer in Glyphs.font.selectedLayers:
    layer.decomposeComponents()
