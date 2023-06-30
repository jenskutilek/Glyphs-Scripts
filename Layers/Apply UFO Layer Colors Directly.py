# MenuTitle: Apply UFO Layer Colors Directly
from AppKit import NSColor
from GlyphsApp import Glyphs


MARK_KEY = "com.typemytype.robofont.mark"

Glyphs.font.disableUpdateInterface()

for selected_layer in Glyphs.font.selectedLayers:
    glyph = selected_layer.parent
    for layer in glyph.layers:
        if MARK_KEY in layer.userData:
            r, g, b, a = layer.userData[MARK_KEY]
            glyph.colorObject = NSColor.colorWithDeviceRed_green_blue_alpha_(
                r, g, b, a
            )
            continue

Glyphs.font.enableUpdateInterface()
