# MenuTitle: Rename Glyphs
from GlyphsApp import Glyphs
from jkFontTools.glyphnames import get_rename_dict

mapping = {
    "tonebarextrahighmod": "toneBarR5",
    "tonebarhighmod": "toneBarR4",
    "tonebarmidmod": "toneBarR3",
    "tonebarlowmod": "toneBarR2",
    "tonebarextralowmod": "toneBarR1",
    "extraHighLeftStemToneBarmod": "toneBarL5",
    "highLeftStemToneBarmod": "toneBarL4",
    "midLeftStemToneBarmod": "toneBarL3",
    "lowLeftStemToneBarmod": "toneBarL2",
    "extraLowLeftStemToneBarmod": "toneBarL1",
}

font = Glyphs.font

d = get_rename_dict(font.glyphs.keys(), mapping)

font.disableUpdateInterface()


# Rename glyphs

for old, new in d.items():
    font.glyphs[old].name = new


# Rename metrics keys
# TODO: Analyze formulas and replace glyph names in them

for g in font.glyphs:
    if g.leftMetricsKey in d:
        g.leftMetricsKey = d[g.leftMetricsKey]
    if g.rightMetricsKey in d:
        g.rightMetricsKey = d[g.rightMetricsKey]


# TODO: Rename in feature code

font.enableUpdateInterface()
