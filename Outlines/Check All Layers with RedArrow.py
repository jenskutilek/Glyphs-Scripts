# MenuTitle: Check All Layers With RedArrow
from redArrow.outlineTestGlyphs import OutlineTest
from redArrow.defaults import default_options, default_tests

from GlyphsApp import Glyphs

ot = OutlineTest(layer=None, options=default_options, run_tests=default_tests)

for g in Glyphs.font.glyphs:
    for layer in g.layers:
        ot.layer = layer
        ot.reset()
        ot.checkLayer()
        if ot.errors:
            print(layer)
            for e in ot.errors:
                print("   ", e)
