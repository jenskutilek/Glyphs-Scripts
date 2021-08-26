# MenuTitle: Delete Backgrounds

from GlyphsApp import Glyphs


__doc__ = """
Deletes all backgrounds from all layers.
"""

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    for l in g.layers:
        l.background = None

Glyphs.font.enableUpdateInterface()