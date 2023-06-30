# MenuTitle: Report Scaled And Mirrored Components
from GlyphsApp import Glyphs

for g in Glyphs.font.glyphs:
    for layer in g.layers:
        for c in layer.components:
            x, y = c.scale
            if abs(x) < 1.0 or abs(y) < 1.0:
                print(f"Scaled component: {layer}, {c.componentName}: ({x}, {y}")
            if x * y < 0:
                print(f"Mirrored component: {layer}, {c.componentName}: ({x}, {y}")
print("End")
