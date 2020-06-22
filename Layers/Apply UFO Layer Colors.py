# MenuTitle: Apply UFO Layer Colors
# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from AppKit import NSColor

color_map = {
    # RGBA to Glyphs color index, see https://docu.glyphsapp.com/#GSLayer.color
    (1.0, 0.6, 0.647, 1.0): 0,  # red
    (1.0, 0.6, 0.6, 1.0): 0,  # red
    (1.0, 0.873, 0.6, 1.0): 1,  # orange
    (1.0, 0.666, 0.6, 1.0): 2,  # brown
    (1.0, 0.976, 0.6, 1.0): 3,  # yellow
    (0.656, 1.0, 0.6, 1.0): 4,  # light green
    (0.619, 1.0, 0.6, 1.0): 4,  # dark green
    (0.6, 0.995, 1.0, 1.0): 6,  # light blue
    (0.6, 0.986, 1.0, 1.0): 6,  # light blue
    (0.6, 0.741, 1.0, 1.0): 7,  # dark blue
    (0.6, 0.609, 1.0, 1.0): 8,  # purple
    (0.967, 0.6, 1.0, 1.0): 9,  # magenta
    (0, 0, 0, 0): 9223372036854775807,  # not colored, white
}

set_colors = True
unset_userdata_colors = False
used_colors = set()

for glyph in Font.glyphs:
    for layer in glyph.layers:
        rgba = layer.userData.get(
            "com.typemytype.robofont.mark",  # Actually also used by vfb2ufo
            None,
        )
        if rgba is None:
            if set_colors:
                layer.color = 9223372036854775807
        else:
            r, g, b, a = rgba
            if set_colors:
                color = color_map.get((r, g, b, a), None)
                if color is None:
                    layer.colorObject = NSColor.colorWithDeviceRed_green_blue_alpha_(
                        r, g, b, a
                    )
                    if (r, g, b, a) not in used_colors:
                        print(
                            "INFO: Unknown color (%g, %g, %g, %g) was applied directly, you may want to add a mapping for it in the script."
                            % (r, g, b, a)
                        )
                else:
                    layer.color = color
            used_colors |= set([(r, g, b, a)])
            if unset_userdata_colors:
                del layer.userData["com.typemytype.robofont.mark"]

        # print(glyph.name, layer, r, g, b, a)

print("Colors used in font:", list(used_colors))
