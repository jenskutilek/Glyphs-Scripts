#MenuTitle: Remove Overlaps MM
from __future__ import absolute_import, division, print_function, unicode_literals

__doc__="""
Remove overlaps in selected glyphs, only if glyphs stay MM-compatible
"""

Glyphs.font.disableUpdateInterface()



for l in Glyphs.font.selectedLayers:
	g = l.parent
	temp = g.duplicate("remove_overlap_temp")
	temp = Glyphs.font.glyphs[temp.name]
	compatible = True
	for tl in temp.layers:
		tl.removeOverlap()
	
	if temp.mastersCompatibleForLayers_([l for l in temp.layers]):
		print("OK: %s" % g.name)
		g.beginUndo()
		for gl in g.layers:
			gl.removeOverlap()
		g.endUndo()
	else:
		print("    Can't remove overlap in glyph: %s" % g.name)
	del(Glyphs.font.glyphs[temp.name])

Glyphs.font.enableUpdateInterface()
