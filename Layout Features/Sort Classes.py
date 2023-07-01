# MenuTitle: Sort Classes By Name And Active Status
from jkGlyphsHelpers.forAll import forCurrentFont

__doc__ = """
Sort OpenType classes of the current font alphabetically by name, and sort inactive
classes towards the end.
"""


def sort_ot_classes(font):
    font.classes = sorted(font.classes, key=lambda x: (not x.active, x.name.casefold()))


forCurrentFont(sort_ot_classes)
