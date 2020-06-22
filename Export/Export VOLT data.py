# MenuTitle: Export VOLT Data
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

glyph_defs = """DEF_GLYPH ".notdef" ID 0 TYPE BASE END_GLYPH
DEF_GLYPH "CR" ID 1 UNICODE 13 TYPE BASE END_GLYPH
DEF_GLYPH "space" ID 2 UNICODE 32 TYPE BASE END_GLYPH
"""

i = 3
for g in Font.glyphs:
    if g.name not in ("space", "CR", ".notdef") and g.export:
        final_name = g.name if g.productionName is None else g.productionName
        if g.unicode is None:
            glyph_defs += 'DEF_GLYPH "%s" ID %i TYPE BASE END_GLYPH\n' % (
                final_name,
                i,
            )
        else:
            glyph_defs += (
                'DEF_GLYPH "%s" ID %i UNICODE %i TYPE BASE END_GLYPH\n'
                % (final_name, i, int(g.unicode, 16))
            )
        i += 1

view_options = """GRID_PPEM 48
PRESENTATION_PPEM 120
PPOSITIONING_PPEM 200
CMAP_FORMAT 0 3 4
CMAP_FORMAT 1 0 6
CMAP_FORMAT 3 1 4 END
"""
