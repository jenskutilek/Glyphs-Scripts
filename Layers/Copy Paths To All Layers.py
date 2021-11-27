# MenuTitle: Copy Paths To All Layers

for layer in Glyphs.font.selectedLayers:
	g = layer.parent
	paths = [p.copy() for p in layer.paths]
	for l in g.layers:
		if layer == l:
			continue
		l.shapes = []
		for p in paths:
			l.paths.append(p.copy())
		l.width = layer.width