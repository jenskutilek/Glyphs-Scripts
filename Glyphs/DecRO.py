# MenuTitle: Copy to Background, Decompose, Remove Overlaps, Correct Path Direction
for layer in Glyphs.font.selectedLayers:
    g = layer.parent
    for l in g.layers:
        l.background = l.copy()
        l.decomposeComponents()
        l.removeOverlap()
        l.correctPathDirection()
