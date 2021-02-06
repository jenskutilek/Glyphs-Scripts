# MenuTitle: Add Corner Components To Selection

layer = Glyphs.font.selectedLayers[0]
for n in Glyphs.font.selectedLayers[0].selection:
	hint = GSHint()
	hint.originNode = n
	hint.type = CORNER
	hint.name = "_corner.universal"
	layer.hints.append(hint)
