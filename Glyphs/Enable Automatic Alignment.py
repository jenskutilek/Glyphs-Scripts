# MenuTitle: Enable Automatic Alignment (Font-specific)
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    for l in g.layers:
        for i in range(len(l.components)):
            c = l.components[i]
            c.automaticAlignment = True
            # c.position = (0, -402)
        l.leftMetricsKey = None
        l.rightMetricsKey = None
    # g.leftMetricsKey = l.components[0].componentName
    # g.rightMetricsKey = l.components[0].componentName
    g.leftMetricsKey = None
    g.rightMetricsKey = None
