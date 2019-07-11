#MenuTitle: Remove Hints

__doc__="""
Remove hints in selected layers
"""

Glyphs.font.disableUpdateInterface()

for l in Glyphs.font.selectedLayers:
	l.hints = []

Glyphs.font.enableUpdateInterface()
