#MenuTitle: Copy Glyphs From Layer For Selection
from __future__ import absolute_import, division, print_function, unicode_literals

from robofab.world import AllFonts, CurrentFont
from robofab.interface.all.dialogs import SelectFont

sm = SelectFont("Select source master")

f = CurrentFont()

selection_names = f.selection[:]

print(sm)

for n in selection_names:
	if n in sm:
		source_glyph = sm[n]
		target_glyph = f[n]
		#print source_glyph.name, len(source_glyph), "contours"
		
		f[n].clear()
		f[n].appendGlyph(source_glyph)
		f[n].width = source_glyph.width
	else:
		print("Glyph '%s' does not exist in source master %s." % (n, sm))
f.update()
