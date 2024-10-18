# MenuTitle: Apply Class Order Imported from UFO

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

    group_order = ufolib.get("public.groupOrder")
    if group_order is None:
        Message("The imported UFO lib does not contain a group order list.")
        return
    font_groups = [c.name for c in font.classes]
    missing = set(font_groups) - set(group_order)
    unsortable = [c for c in font.classes if c.name in missing]
    sortable = {c.name: c for c in font.classes if c.name not in missing}

    # Filter duplicates and sort by index in group_order
    sorted_groups = sorted(list(sortable.values()),
                           key=lambda x: (group_order.index(x.name)))
    # print([g.name for g in sorted_groups])

    font.classes = sorted_groups + unsortable


forCurrentFont(sort_ot_classes)
