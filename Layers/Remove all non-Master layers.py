# MenuTitle: Remove all non-Master layers
from GlyphsApp import Glyphs

__doc__ = """
Goes through selected glyphs and deletes all glyph layers which are not a Master,
Bracket or Brace layer.
"""


font = Glyphs.font
selectedLayers = font.selectedLayers


def process(thisGlyph):
    count = 0
    numberOfLayers = len(thisGlyph.layers)
    for i in range(numberOfLayers)[::-1]:
        thisLayer = thisGlyph.layers[i]
        if not thisLayer.isSpecialLayer and not thisLayer.isMasterLayer:
            count += 1
            del thisGlyph.layers[i]
    return count


font.disableUpdateInterface()

for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent
    thisGlyphName = thisGlyph.name

    if str(thisGlyphName)[:7] != "_smart.":
        thisGlyph.beginUndo()
        print("%s layers deleted in %s." % (process(thisGlyph), thisGlyphName))
        thisGlyph.endUndo()
    else:
        print("Smart layers kept in %s." % (thisGlyphName))

font.enableUpdateInterface()
