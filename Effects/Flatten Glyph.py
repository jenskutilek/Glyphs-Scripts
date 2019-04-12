# MenuTitle: Flatten Glyph MM
from __future__ import absolute_import, division, print_function

from fontTools.misc.bezierTools import calcCubicArcLength

master_names = ["Medium 9 Clean", "Medium 8 Clean"]

masters = {
	master.name: master.id
	for master in Font.masters
}


def measureGlyph(g):
	print(g)
	arc_lengths = {}
	for master_name in master_names:
		arc_lengths[master_name] = {}
		layer = g.layers[masters[master_name]]
		print(layer)
		for i in range(len(layer.paths)):
			path = layer.paths[i]
			for j in range(len(path.segments)):
				s = path.segments[j]
				if len(s) == 4:
					# curve
					p0, p1, p2, p3 = s
					p0 = p0.x, p0.y
					p1 = p1.x, p1.y
					p2 = p2.x, p2.y
					p3 = p3.x, p3.y
					arc_lengths[master_name][(i, j)] = int(round(calcCubicArcLength(p0, p1, p2, p3)))

	return arc_lengths


arc_lengths = measureGlyph(Font.selectedLayers[0].parent)
print(arc_lengths)
