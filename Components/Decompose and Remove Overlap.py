#MenuTitle: Decompose And Remove Overlap For Selection

for l in Glyphs.font.selectedLayers:
	l.decomposeComponents()
	l.removeOverlap()
