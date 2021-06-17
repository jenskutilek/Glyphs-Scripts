# MenuTitle: Copy Paths From Background To Layer

for l in Glyphs.font.selectedLayers:
	l.paths = []
	l.components = []
	for p in l.background.paths:
		l.paths.append(p.copy())
	
