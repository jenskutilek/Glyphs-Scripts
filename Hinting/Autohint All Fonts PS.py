#MenuTitle: Autohint All Fonts (PS)
print "Autohinting ..."

for f in Glyphs.fonts:
	print "    %s" % f
	for g in Glyphs.font.glyphs:
		#for l in g.layers:
		#	l.autohint()
		g.layers[0].autohint()

