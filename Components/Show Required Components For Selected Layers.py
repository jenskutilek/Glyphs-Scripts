# MenuTitle: Show Required Components For Selected Layers

from GlyphsApp import Glyphs

parts = set()
for l in Glyphs.font.selectedLayers:
    parts |= set((l.parent.name,))
    for c in l.components:
        parts |= set((c.componentName,))
for part in sorted(parts):
    print(part)
