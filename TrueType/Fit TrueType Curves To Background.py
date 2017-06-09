#MenuTitle: Fit TrueType Curves To Background

from jkRFTools.fitquadratic.FunctionsGlyphs import fit_layer


def optimize_selected():
	f = Glyphs.font
	for layer in f.selectedLayers:
		if len(layer.paths) > 0:
			print "Processing %s ..." % layer.parent.name
			selection_only = False #len(layer.selection) > 0
			fit_layer(layer, selection_only)


if __name__ == "__main__":
	optimize_selected()
