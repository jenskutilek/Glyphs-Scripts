#MenuTitle: Copy Glyphs From Layer For Selection

from robofab.world import AllFonts, CurrentFont
from robofab.interface.all.dialogs import SelectFont

sm = SelectFont("Select source master")

f = CurrentFont()

selection_names = f.selection[:]

print sm

for n in selection_names:
	print n
	source_glyph = sm[n]
	print source_glyph.name, len(source_glyph), "contours"
	f[n].clear()
	f[n].appendGlyph(source_glyph)
f.update()
