#MenuTitle: Add Tone Mirrored Components
from __future__ import absolute_import, division, print_function, unicode_literals

tones = {
	"tonebarextrahighmod": "extraHighLeftStemToneBarmod",
	"tonebarhighmod":      "highLeftStemToneBarmod",
	"tonebarmidmod":       "midLeftStemToneBarmod",
	"tonebarlowmod":       "lowLeftStemToneBarmod",
	"tonebarextralowmod":  "extraLowLeftStemToneBarmod",
}


def add_mirror_component(src, tgt):
	if src in Font.glyphs:
		Font.glyphs.append(GSGlyph(tgt))
		tg = Font.glyphs[tgt]
		for l in tg.layers:
			comp = GSComponent(src)
			comp.transform = ((
				-1.0, # x scale factor
				0.0, # x skew factor
				0.0, # y skew factor
				1.0, # y scale factor
				0.0, # x position
				0.0  # y position
			))
			comp.automaticAlignment = True
			l.components.append(comp)
	else:
		print "# Source glyph not found:", src

# TODO: Use shorter ligature names (uni names?)
# FDK can't compile the 3-tone ligatures


for name, left in tones.items():
	for name2, left2 in tones.items():
		if name != name2:
			source_name = "%s_%s" % (name2, name)
			target_name = "%s_%s" % (left, left2)
			add_mirror_component(source_name, target_name)
		for name3, left3 in tones.items():
			if len(set([name, name2, name3])) != 1:
				source_name = "%s_%s_%s" % (name3, name2, name)
				target_name = "%s_%s_%s" % (left, left2, left3)
				print "sub %s %s %s by %s_%s_%s;" % (left, left2, left3, left, left2, left3)
				add_mirror_component(source_name, target_name)
		print "sub %s %s by %s_%s;" % (left, left2, left, left2)
			
