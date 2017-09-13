# MenuTitle: Export VTT CharGroups

f = Font

data = '''/*****

CharGrp.txt

These columns are:

Microsoft Unicode (character code)
          Mac code
                  Apple Unicode
                            Glyph index
                                   Character group
                                   you may have to correct and/or extend this
                                   to match the groups chosen in CvtTmpl.txt
                                                PostScript Name

0x0000    0x00    0x0000      0    <--- Minimum value
0xFFEE    0xFF    0xFFEE  65518    <--- Maximum value

*****/

'''

glyph_groups = {
	("Letter", "Uppercase"):     "UPPERCASE",
	("Letter", "Lowercase"):     "LOWERCASE",
	("Number", "Decimal Digit"): "FIGURE",
	("Number", "Other"):         "FIGURE",
	
}

def get_glyphgroup(g):
	group = glyph_groups.get((g.category, g.subCategory), "OTHER")
	return group
	

i = 3
for g in f.glyphs:
	if g.export:
		final_name = g.name if g.productionName is None else g.productionName
		if g.unicode is None:
			u = None
			if "." in g.name:
				base_name = g.name.split(".", 1)[0]
				if base_name in f.glyphs:
					u = f.glyphs[base_name].unicode
			elif "_" in g.name:
				base_name = g.name.split("_", 1)[0]
				if base_name in f.glyphs:
					u = f.glyphs[base_name].unicode
			if u is not None:
				u = int(u, 16)
		else:
			u = int(g.unicode, 16)
		
		group = get_glyphgroup(g)
		
		if u is None:
			data += '*         *       *         %5i    %9s    %s\n' % (i, group, final_name)
		else:
			data += '0x%04X    *       0x%04X    %5i    %9s    %s\n' % (u, u, i, group, final_name)
		
		i += 1

print data

