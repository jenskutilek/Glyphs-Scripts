#MenuTitle: Rename Glyphs
from __future__ import absolute_import, division, print_function, unicode_literals

from jkFontTools.glyphnames import get_rename_dict

mapping = {
	"tonebarextrahighmod": "toneBarR5",
	"tonebarhighmod":      "toneBarR4",
	"tonebarmidmod":       "toneBarR3",
	"tonebarlowmod":       "toneBarR2",
	"tonebarextralowmod":  "toneBarR1",
	
	"extraHighLeftStemToneBarmod": "toneBarL5",
	"highLeftStemToneBarmod":      "toneBarL4",
	"midLeftStemToneBarmod":       "toneBarL3",
	"lowLeftStemToneBarmod":       "toneBarL2",
	"extraLowLeftStemToneBarmod":  "toneBarL1",
}

d = get_rename_dict(Font.glyphs.keys(), mapping)

Font.disableUpdateInterface()


# Rename glyphs

for old, new in d.items():
	Font.glyphs[old].name = new


# Rename metrics keys
# TODO: Analyze formulas and replace glyph names in them

for g in Font.glyphs:
	if g.leftMetricsKey in d:
		g.leftMetricsKey = d[g.leftMetricsKey]
	if g.rightMetricsKey in d:
		g.rightMetricsKey = d[g.rightMetricsKey]


# TODO: Rename in feature code

Font.enableUpdateInterface()
