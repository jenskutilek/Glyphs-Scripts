# MenuTitle: Print Global Glyph Set

ggo = []

for f in Glyphs.fonts:
	ggo += [g.name for g in f.glyphs if g.export]

ggo = list(set(ggo))
print(" ".join(ggo))
