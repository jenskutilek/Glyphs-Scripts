# MenuTitle: Report Nested Components
from GlyphsApp import Glyphs


flatten = False

for g in Glyphs.font.glyphs:
    if not g.export:
        continue

    for layer in g.layers:
        for c in layer.components:
            base = c.component.layers[layer.layerId]
            if hasattr(base, "components"):
                if base.components and not base.paths:
                    if not flatten:
                        print(f"Nested component: {c.componentName} in glyph {g.name} {layer.name}")
                    if flatten:
                        if layer.anchors:
                            print(f"Anchors existed in {g.name}, please fix manually")
                            continue

                        for cc in layer.components:
                            cc.automaticAlignment = False
                        c.decompose()
