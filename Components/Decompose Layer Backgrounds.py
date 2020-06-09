#MenuTitle: Decompose Background Layers For Selection
from __future__ import absolute_import, division, print_function, unicode_literals

for g in Glyphs.font.glyphs:
	for l in g.layers:
		b = l.background
		b.decomposeComponents()
