# MenuTitle: Draw Circles at Oncurve Points

from GlyphsApp import GSNode, GSPath, CURVE, OFFCURVE, Layer
# from jkGlyphsTools.drawing import drawCircle


def drawCircle(layer, x, y, size=50, roundness=0.551970):
	hs = int(round(.5 * size))
	hsr = int(round(.5 * size * roundness))
	path = GSPath()

	path.nodes.append(GSNode((x-hsr, y+hs), OFFCURVE))
	path.nodes.append(GSNode((x-hs, y+hsr), OFFCURVE))
	path.nodes.append(GSNode((x-hs, y), CURVE))
	
	path.nodes.append(GSNode((x-hs, y-hsr), OFFCURVE))
	path.nodes.append(GSNode((x-hsr, y-hs), OFFCURVE))
	path.nodes.append(GSNode((x, y-hs), CURVE))
	
	path.nodes.append(GSNode((x+hsr, y-hs), OFFCURVE))
	path.nodes.append(GSNode((x+hs, y-hsr), OFFCURVE))
	path.nodes.append(GSNode((x+hs, y), CURVE))
	
	path.nodes.append(GSNode((x+hs, y+hsr), OFFCURVE))
	path.nodes.append(GSNode((x+hsr, y+hs), OFFCURVE))
	path.nodes.append(GSNode((x, y+hs), CURVE))
	
	path.closed = True

	layer.paths.append(path)


coords = []
for p in Layer.paths:
	for n in p.nodes:
		if n.type != OFFCURVE:
			coords.append(
				(
					int(round(n.x)),
					int(round(n.y))
				)
			)
for x, y in coords:
	drawCircle(Layer, x, y)