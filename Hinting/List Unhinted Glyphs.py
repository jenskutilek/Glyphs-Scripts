# MenuTitle: List Unhinted Glyphs
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
List unhinted glyphs in current font
"""

for g in Font.glyphs:
    if len(g.layers[0].paths) > 0:
        if not g.layers[0].hints:
            print(g.name)
