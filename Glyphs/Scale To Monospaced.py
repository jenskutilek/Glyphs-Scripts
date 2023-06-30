# MenuTitle: Scale To Monospaced
from GlyphsApp import Glyphs

layer = Glyphs.font.selectedLayers[0]  # current layer


def scaleLayer(layer, width):

    print(layer.parent.name, layer.width)

    x_scale = width / layer.width

    print(x_scale)

    layer.applyTransform(
        [
            x_scale,  # x scale factor
            0.0,  # x skew factor
            0.0,  # y skew factor
            1.0,  # y scale factor
            0.0,  # x position
            0.0,  # y position
        ]
    )

    layer.width = width


for layer in Glyphs.font.selectedLayers:
    scaleLayer(layer, 600)
