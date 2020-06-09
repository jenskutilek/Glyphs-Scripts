#MenuTitle: Make Unitized Template Font
from __future__ import absolute_import, division, print_function, unicode_literals

from jkRFoTools.unitization import unitization_info

sc = unitization_info.get_systems_by_upm(9)[0] # IBM Selectric Composer, 3-9 units

print(sc.fixed_units)

# 900 upm are assumed for now
upm = Glyphs.font.upm

for u, chars in sc.fixed_units.items():
	for c in chars:
		g = GSGlyph("uni%04X" % ord(c))
		try:
			Glyphs.font.glyphs.append(g)
		except:
			g = Glyphs.font.glyphs[c]
		g.unicode = hex(ord(c))
		g.layers[0].width = u * 100
