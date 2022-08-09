# MenuTitle: Sort Classes By Name And Active Status
__doc__="""
Sort OpenType classes alphabetically by name, and sort inactive classes to the
end.
"""

f = Glyphs.font
f.classes = sorted(f.classes, key=lambda x: (not x.active, x.name.casefold()))
