# MenuTitle: Format Classes
__doc__="""
Format all OpenType classes to contain one glyph name per line.
"""


for c in Glyphs.font.classes:
	c.code = c.code.replace(" ", "\n")
