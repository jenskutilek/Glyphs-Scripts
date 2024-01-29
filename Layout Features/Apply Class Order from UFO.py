#MenuTitle: Apply Class Order Imported from UFO

from GlyphsApp import Message
from jkGlyphsHelpers.forAll import forCurrentFont

__doc__ = """
For Glyphs files that have been converted with vfb3ufo, this restores the original sort
order of OpenType classes.
"""


def sort_ot_classes(font):
    ufolib = font.userData.get("UFO.lib")
    if ufolib is None:
        Message("The file does not contain an imported UFO lib.")
        return

    group_order = ufolib.get("com.lucasfonts.vfblib.groupOrder")
    if group_order is None:
        Message("The imported UFO lib does not contain a group order list.")
        return

    # Filter duplicates and sort by index in group_order
    font.classes = sorted(
        list({c.name: c for c in font.classes}.values()),
        key=lambda x: (group_order.index(x.name)),
    )


forCurrentFont(sort_ot_classes)
