#MenuTitle: Remove Hints

__doc__="""
Remove hints in selected glyphs
"""

Glyphs.font.disableUpdateInterface()


for l in Glyphs.font.selectedLayers:
	g = l.parent
	for gl in g.layers:
		gl.hints = []

Glyphs.font.enableUpdateInterface()
