# MenuTitle: Autohint Selection
from jkGlyphsHelpers.forSelected import forSelectedLayers

__doc__ = """
Autohint selected layers
"""


def autohint_layer(layer):
    layer.autohint()


forSelectedLayers(autohint_layer)
