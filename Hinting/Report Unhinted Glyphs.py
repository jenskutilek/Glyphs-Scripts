# MenuTitle: Report Unhinted Glyphs
from GlyphsApp import Glyphs

__doc__ = """
Report unhinted glyphs in current font
"""

for g in Glyphs.font.glyphs:
    if len(g.layers[0].paths) > 0:
        if not g.layers[0].hints:
            print(g.name)
print("End")
