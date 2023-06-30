# MenuTitle: Autohint Selection
from GlyphsApp import Glyphs
from jkGlyphsScripts.forSelected import forSelectedLayers

__doc__ = """
Autohint selected layers
"""


def autohint_layer(layer):
    layer.autohint()


forSelectedLayers(Glyphs.font, autohint_layer)
