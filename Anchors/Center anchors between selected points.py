# MenuTitle: Center anchors between selected points
from __future__ import absolute_import, division, print_function, unicode_literals

from math import ceil
selection = Layer.selection
x = sorted([obj.x for obj in selection if type(obj) == GSNode])
a = [obj for obj in selection if type(obj) == GSAnchor]
if x and a:
	ax = int(ceil((x[0] + x[-1]) / 2))
	for anchor in a:
		anchor.x = ax
