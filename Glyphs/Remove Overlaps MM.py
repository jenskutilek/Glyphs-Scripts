#MenuTitle: Remove Overlaps MM

__doc__="""
Remove overlaps in selected glyphs, only if glyphs stay MM-compatible
"""

Glyphs.font.disableUpdateInterface()



for l in Glyphs.font.selectedLayers:
	g = l.parent
	#print g.name, g.mastersCompatible
	temp = g.duplicate("remove_overlap_temp")
	temp = Glyphs.font.glyphs[temp.name]
	#temp.beginUndo()
	for tl in temp.layers:
		tl.removeOverlap()
	#temp.endUndo()
	
	if temp.mastersCompatible:
		print "Compatible"
		g.beginUndo()
		for gl in g.layers:
			gl.removeOverlap()
		g.endUndo()
	else:
		print "    Can't remove overlap in glyph: %s" % g.name
	#print g.name, g.mastersCompatible
	del(Glyphs.font.glyphs[temp.name])

Glyphs.font.enableUpdateInterface()
