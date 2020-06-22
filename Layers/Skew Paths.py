# MenuTitle: Skew only Paths and Anchors
# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
"""

import GlyphsApp
import math
from AppKit import NSAffineTransform


def slantLayers(layers, angle):
    Font.disableUpdateInterface()
    xHeight = layers[0].associatedFontMaster().xHeight
    transform = NSAffineTransform.new()
    slant = math.tan(skewAngle * math.pi / 180.0)
    transform.shearXBy_atCenter_(slant, -xHeight / 2.0)

    for layer in selectedLayers:
        for path in layer.paths:
            for node in path.nodes:
                node.position = transform.transformPoint_(node.position)
        for anchor in layer.anchors:
            anchor.position = transform.transformPoint_(anchor.position)

    Font.enableUpdateInterface()


skewAngle = 13
slantLayers(Glyphs.font.selectedLayers, skewAngle)
