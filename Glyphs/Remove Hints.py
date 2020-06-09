#MenuTitle: Remove Hints
from __future__ import absolute_import, division, print_function, unicode_literals

__doc__="""
Remove hints in selected glyphs
"""

Glyphs.font.disableUpdateInterface()

for l in Glyphs.font.selectedLayers:
	g = l.parent
	for gl in g.layers:
		gl.hints = []

Glyphs.font.enableUpdateInterface()
