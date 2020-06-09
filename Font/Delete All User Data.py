#MenuTitle: Delete All User Data
from __future__ import absolute_import, division, print_function, unicode_literals

__doc__="""
Delete all hidden user data from the current font, e.g. for cleaning up after importing a UFO.
"""

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
	ud = g.userData
	if ud:
		print(g.name)
		for key in ud.keys():
			print "   ", key
			print "       ", ud[key]
			del ud[key]
	for layer in g.layers:
		ud = layer.userData
		if ud:
			print g.name
			for key in ud.keys():
				print "   ", key
				print "       ", ud[key]
				del ud[key]

Glyphs.font.enableUpdateInterface()
