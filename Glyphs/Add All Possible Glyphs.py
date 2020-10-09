infos = GSGlyphsInfo.alloc().init()
font = Glyphs.font

build_glyphs = False
names = []

for info in infos.glyphInfos():
	if not info.components or info.name in font.glyphs or info.name.endswith(".half") or info.name.endswith(".full") or info.name.endswith("mod") or info.name.endswith("-math"):
		continue

	component_missing = False
	for c in info.components:
		if c.name not in font.glyphs:
			# print "Skipping %s because of missing component %s..." % (info.name, c.name)
			component_missing = True
			break

	if component_missing:
		continue
	
	if build_glyphs:

		glyph = GSGlyph(info.name)
		font.glyphs.append(GSGlyph(info.name))
		glyph = Glyphs.font.glyphs[info.name]
		for layer in glyph.layers:
			for c in info.components:
				layer.components.append(GSComponent(c.name))
	else:
		names.append(info.name)

print " ".join(names)
