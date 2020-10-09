g = Glyphs.font.glyphs
for i in GSGlyphsInfo.alloc().init().glyphInfos():
    if i.components and i.name not in g and all(c.name in g for c in i.components):
        print i.name
