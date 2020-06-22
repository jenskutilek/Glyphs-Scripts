# MenuTitle: Report unrecognized anchor names for mark feature
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from re import compile

an = compile("^(_)?[a-z]+(_[123])?$")

for g in Glyphs.font.glyphs:
    layer = g.layers[0]
    for a in layer.anchors:
        if not an.match(a.name):
            print(g.name, a.name)
print("OK")
