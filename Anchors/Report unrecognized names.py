# MenuTitle: Report unrecognized anchor names for mark feature

from re import compile

an = compile("^(_)?[a-z]+(_[123])?$")

for g in Glyphs.font.glyphs:
	layer = g.layers[0]
	for a in layer.anchors:
		if not an.match(a.name):
			print g.name, a.name
print "OK"
