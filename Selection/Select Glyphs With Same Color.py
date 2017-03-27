#MenuTitle: Select Glyphs With Same Color

__doc__="""
Select all glyphs which have the same color as the currently selected glyph(s).
"""

def getColorsForSelection(font):
	# Collect master colors
	colors = list(set([l.parent.color for l in font.selectedLayers]))
	# Collect layer colors except for white
	colors += list(set([l.color for l in font.selectedLayers if l.color != 9223372036854775807]))
	return colors

def getGlyphNamesByColors(font, colors):
	selection = [g.name for g in font.glyphs if g.color in colors]
	return selection

def setSelection(font, glyph_names, deselect=False):
	if deselect:
		for g in font.glyphs:
			g.selected = False
	for g in glyph_names:
		font.glyphs[g].selected = True
		
def selectGlyphsWithSameColor(font):
	font.disableUpdateInterface()
	colors = getColorsForSelection(font)
	selection = getGlyphNamesByColors(font, colors)
	setSelection(font, selection)
	font.enableUpdateInterface()
	

if __name__ == "__main__":
	selectGlyphsWithSameColor(Glyphs.font)
