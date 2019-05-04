# MenuTitle: Apply UFO Layer Colors
# -*- coding: utf-8 -*-
from __future__ import print_function

color_map = {
    (1.0, 0.666, 0.6, 1.0): 2,
    (1.0, 0.6, 0.647, 1.0): 0,
    (0.6, 0.995, 1.0, 1.0): 6,
    (0.656, 1.0, 0.6, 1.0): 4,
    (0.619, 1.0, 0.6, 1.0): 4,
    (1.0, 0.6, 0.6, 1.0):   0,
    (0.6, 0.741, 1.0, 1.0): 7,
    (1.0, 0.976, 0.6, 1.0): 3,
    (1.0, 0.873, 0.6, 1.0): 1,
    (0.6, 0.609, 1.0, 1.0): 8,
    (0.967, 0.6, 1.0, 1.0): 9,
    (0.6, 0.986, 1.0, 1.0): 6,
}

set_colors = True
used_colors = set()

for glyph in Font.glyphs:
    for layer in glyph.layers:
        rgba = layer.userData.get("com.typemytype.robofont.mark", (0, 0, 0, 0))
        if rgba is None:
            if set_colors:
                layer.color = 9223372036854775807
        else:
            r, g, b, a = rgba
            if set_colors:
                layer.color = color_map.get((r, g, b, a), 9223372036854775807)
            else:
                used_colors |= set([(r, g, b, a)])

        # print(glyph.name, layer, r, g, b, a)

print(list(used_colors))
