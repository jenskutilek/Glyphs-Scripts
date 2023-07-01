# MenuTitle: Skew Only Paths and Anchors By 13 Degrees
from AppKit import NSAffineTransform
from GlyphsApp import Glyphs
from jkGlyphsHelpers.forSelected import forSelectedLayers
import math

__doc__ = """
Slant Selected Layers by 13 degrees.
"""


def slantLayer(layer, transform):
    for path in layer.paths:
        for node in path.nodes:
            node.position = transform.transformPoint_(node.position)
    for anchor in layer.anchors:
        anchor.position = transform.transformPoint_(anchor.position)


def slantLayers(layers, angle):
    xHeight = layers[0].associatedFontMaster().xHeight
    transform = NSAffineTransform.new()
    slant = math.tan(skewAngle * math.pi / 180.0)
    transform.shearXBy_atCenter_(slant, -xHeight / 2.0)

    forSelectedLayers(slantLayer, transform=transform)


skewAngle = 13
slantLayers(Glyphs.font.selectedLayers, skewAngle)
