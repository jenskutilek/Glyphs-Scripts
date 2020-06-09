# MenuTitle: Report Width Differences
from __future__ import absolute_import, division, print_function, unicode_literals

sf = Glyphs.font
sm = sf.selectedFontMaster

for tf in Glyphs.fonts:
	if tf != sf:
		tm = tf.selectedFontMaster
		break

missing = []

for g in sf.glyphs:
	sl = g.layers[sm.id]
	if g.name in tf.glyphs:
		tg = tf.glyphs[g.name]
		tl = tg.layers[tf.selectedFontMaster.id]
		if sl.width != tl.width:
			print("%s;%s;%s;" % (g.name, sl.width, tl.width))
	else:
		#	print("%s;%s;;" % (g.name, " ".join(sc)))
		if not (g.name.endswith(".sc") or g.name.endswith(".pcap")):
			missing.append(g.name)

print("\nMissing in target:\n")
print("\n".join(missing))
