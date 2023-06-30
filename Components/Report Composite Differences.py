# MenuTitle: Report Composite Differences
from GlyphsApp import Glyphs

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
        sc = [c.baseGlyph for c in sl.components]
        tc = [c.baseGlyph for c in tl.components]
        if tc != sc:
            print("%s;%s;%s;" % (g.name, " ".join(sc), " ".join(tc)))
    else:
        # 	print "%s;%s;;" % (g.name, " ".join(sc))
        if not (g.name.endswith(".sc") or g.name.endswith(".pcap")):
            missing.append(g.name)

print("\nMissing in target:\n")
print("\n".join(missing))
