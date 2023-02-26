# MenuTitle: Reinterpolate Selected Layers
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from GlyphsApp import Glyphs

__doc__ = """
Reinterpolate the selected layers.
"""

Glyphs.font.disableUpdateInterface()

for layer in Glyphs.font.selectedLayers:
    layer.reinterpolate()

Glyphs.font.enableUpdateInterface()
