# MenuTitle: Autohint All Fonts (PS)
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

print("Autohinting ...")

for f in Glyphs.fonts:
    print("    %s" % f)
    for g in Glyphs.font.glyphs:
        # for l in g.layers:
        # 	l.autohint()
        g.layers[0].autohint()
