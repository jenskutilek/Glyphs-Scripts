# MenuTitle: Center anchors between selected points
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Select anchors and points, then run this script to horizontally center the anchor(s) between the selected points. If no points are selected, the anchors are centered in the layer's width.
"""

from math import ceil
from GlyphsApp import GSAnchor, GSNode

selection = Layer.selection
x = sorted([obj.x for obj in selection if type(obj) == GSNode])
a = [obj for obj in selection if type(obj) == GSAnchor]
if a:
    if x:
        ax = int(ceil((x[0] + x[-1]) / 2))
    else:
        # Center in width
        ax = int(ceil(Layer.width / 2))
    for anchor in a:
        anchor.x = ax
