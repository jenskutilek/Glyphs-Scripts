# MenuTitle: Check Widths Against Other Fonts

sf = Glyphs.font

for tf in Glyphs.fonts:
	if tf == sf:
		continue
	for g in sf.glyphs:
		tg = tf.glyphs[g.name]
		if tg is None:
			print "Missing glyph:", g.name
			continue
		if g.layers[0].width != tg.layers[0].width:
			print g.name
			tg.color = 1
			tg.layers[0].width = g.layers[0].width
