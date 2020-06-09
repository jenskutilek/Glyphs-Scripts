#MenuTitle: Disable Automatic Alignment
from __future__ import absolute_import, division, print_function, unicode_literals

glyphs = [l.parent for l in Glyphs.font.selectedLayers]

Glyphs.font.disableUpdateInterface()

for g in glyphs:
	for l in g.layers:
		for c in l.components:
			c.automaticAlignment = False
	
Glyphs.font.enableUpdateInterface()
