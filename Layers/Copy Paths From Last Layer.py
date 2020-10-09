# MenuTitle: Copy Paths From Last Layer

l = Glyphs.font.selectedLayers[0]
l.paths = []
for p in l.parent.layers[-1].paths:
	l.paths.append(p.copy())
	
