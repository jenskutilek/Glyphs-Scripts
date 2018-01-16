#MenuTitle: Remove Hints

__doc__="""
Remove hints in all glyphs of the current font
"""

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
	for gl in g.layers:
		gl.hints = []

Glyphs.font.enableUpdateInterface()
