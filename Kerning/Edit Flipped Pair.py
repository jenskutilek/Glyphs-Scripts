# MenuTitle: Edit Flipped Pair
from GlyphsApp import Glyphs

__doc__ = """
In the Edit Tab, flip the glyphs to the left and the right of the cursor. Allows editing
the corresponding kerning of symmetric pairs more easily.
"""


tab = Glyphs.font.currentTab
pos = tab.layersCursor
if pos > 0 and pos < len(tab.layers):
    before = tab.layers[: pos - 1]
    L = tab.layers[pos - 1]
    R = tab.layers[pos]
    after = tab.layers[pos + 1 :]
    tab.layers = before + [R, L] + after
    tab.layersCursor = pos
