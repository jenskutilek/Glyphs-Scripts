# MenuTitle: Autohint PS
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Autohint selected layers
"""

Glyphs.font.disableUpdateInterface()

for l in Glyphs.font.selectedLayers:
    l.autohint()

Glyphs.font.enableUpdateInterface()
