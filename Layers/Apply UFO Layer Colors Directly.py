# MenuTitle: Apply UFO Layer Colors Directly
from AppKit import NSColor
from GlyphsApp import Glyphs
from jkGlyphsScripts.forSelected import forAllLayersOfSelectedGlyphs


MARK_KEY = "com.typemytype.robofont.mark"


def applyMarkColor(layer):
    if MARK_KEY in layer.userData:
        r, g, b, a = layer.userData[MARK_KEY]
        layer.parent.colorObject = NSColor.colorWithDeviceRed_green_blue_alpha_(
            r, g, b, a
        )


forAllLayersOfSelectedGlyphs(Glyphs.font, applyMarkColor)
