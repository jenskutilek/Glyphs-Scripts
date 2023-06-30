# MenuTitle: Copy From Last Layer
from GlyphsApp import Glyphs, GSComponent

l = Glyphs.font.selectedLayers[0]
cl = l.parent.layers[-1]
if cl.components:
	l.paths = []
	for c in cl.components:
		l.components.append(GSComponent(c.componentName, c.position))
