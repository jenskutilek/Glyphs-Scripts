#MenuTitle: Decompose Background Layers For Selection

for g in Glyphs.font.glyphs:
	for l in g.layers:
		b = l.background
		b.decomposeComponents()
