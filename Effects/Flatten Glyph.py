# MenuTitle: Flatten Glyph MM
from __future__ import absolute_import, division, print_function

from fontTools.misc.bezierTools import calcCubicArcLength
from math import ceil, sqrt

master_names = ["Medium 9 Clean", "Medium 8 Clean"]

masters = {
	master.name: master.id
	for master in Font.masters
}


def measureGlyph(glyph):
	"""Measure the segment lengths of all layers given in master_names.
	Returns a dictionary with keys of (path_index, segment_index) and
	values of a list of segment lengths.
	"""
	lengths = {}
	# Reference layer, just used for counting paths and segments
	ref_layer = glyph.layers[masters[master_names[0]]]
	for i in range(len(ref_layer.paths)):
		for j in range(len(ref_layer.paths[i].segments)):
			segment_lengths = []
			for master_name in master_names:
				layer = glyph.layers[masters[master_name]]
				s = layer.paths[i].segments[j]
				if len(s) == 4:
					# curve
					p0, p1, p2, p3 = s
					p0 = p0.x, p0.y
					p1 = p1.x, p1.y
					p2 = p2.x, p2.y
					p3 = p3.x, p3.y
					l = calcCubicArcLength(p0, p1, p2, p3)
				elif len(s) == 2:
					p0, p1 = s
					l = sqrt((p1.y - p0.y)**2 + (p1.x - p0.x)**2)
				else:
					print("Unknown segment type:", s)
					l = 0
				segment_lengths.append(int(round(l)))
			lengths[(i, j)] = segment_lengths
	return lengths


def calculateFlatNumbers(segment_lengths, length=30):
	"""Calculate the number of flat segments each segment should be split into.
	Each resulting segment should have approximately the given length.
	"""
	return [
		int(ceil(max(segment_lengths[k]) / length))
		for k in sorted(segment_lengths, reverse=True)
	]


arc_lengths = measureGlyph(Font.selectedLayers[0].parent)
print(arc_lengths)
splits = calculateFlatNumbers(arc_lengths, 10)
print(splits)
