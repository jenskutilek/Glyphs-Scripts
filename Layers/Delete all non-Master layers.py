# MenuTitle: Delete all non-Master layers
# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Goes through selected glyphs and deletes all glyph layers which are not a Master, Bracket or Brace layer.
"""
Font = Glyphs.font
selectedLayers = Font.selectedLayers

def process(thisGlyph):
    count = 0
    numberOfLayers = len(thisGlyph.layers)
    for i in range(numberOfLayers)[::-1]:
        thisLayer = thisGlyph.layers[i]
        if not thisLayer.isSpecialLayer and not thisLayer.isMasterLayer:
            count += 1
            del thisGlyph.layers[i]
    return count

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent
    thisGlyphName = thisGlyph.name

    if str(thisGlyphName)[:7] != "_smart.":
        thisGlyph.beginUndo()
        print("%s layers deleted in %s." % (process(thisGlyph), thisGlyphName))
        thisGlyph.endUndo()
    else:
        print("Smart layers kept in %s." % (thisGlyphName))

Font.enableUpdateInterface()
