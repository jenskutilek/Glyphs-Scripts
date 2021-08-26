# MenuTitle: Assign Exception Layers To First Master

from GlyphsApp import Glyphs

__doc__ = """
Assign all exception layers to the first master. This is not strictly necessary,
but it simplifies building the fonts with fontmake via glyphsLib.
"""

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    for layer in g.layers:
        attrs = layer.attributes
        if layer.layerId != layer.associatedMasterId and "coordinates" in attrs:
            locs = [
                attrs["coordinates"][k]
                for k in sorted(attrs["coordinates"].keys())
            ]
            name = "{%s}" % ", ".join(locs)
            layer.name = name

Glyphs.font.enableUpdateInterface()
