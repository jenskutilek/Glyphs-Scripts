# MenuTitle: Add Components To Selection
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Expand the current selection by all components necessary to build the selected glyph(s).
"""


def setSelection(font, glyph_names, deselect=False):
    if deselect:
        for g in font.glyphs:
            g.selected = False
    for g in glyph_names:
        font.glyphs[g].selected = True


bases = []
components = []
for l in Glyphs.font.selectedLayers:
    bases.append(l.parent.name)
    for c in l.components:
        if c.componentName not in components:
            components.append(c.componentName)

setSelection(Glyphs.font, bases + components)
