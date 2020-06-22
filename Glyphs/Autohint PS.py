# MenuTitle: Autohint PS
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Autohint all layers of selected glyphs
"""

Glyphs.font.disableUpdateInterface()

for l in Glyphs.font.selectedLayers:
    g = l.parent
    for gl in g.layers:
        gl.autohint()

Glyphs.font.enableUpdateInterface()
