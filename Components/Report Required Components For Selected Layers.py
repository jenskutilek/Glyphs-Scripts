# MenuTitle: Report Required Components For Selected Layers
from GlyphsApp import Glyphs

parts = set()
for layer in Glyphs.font.selectedLayers:
    parts |= set((layer.parent.name,))
    for c in layer.components:
        parts |= set((c.componentName,))
for part in sorted(parts):
    print(part)
