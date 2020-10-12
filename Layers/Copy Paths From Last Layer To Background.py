# MenuTitle: Copy Paths From Last Layer To Background

for l in Glyphs.font.selectedLayers:
	l.background.paths = []
	for p in l.parent.layers[-1].paths:
		l.background.paths.append(p.copy())
	
