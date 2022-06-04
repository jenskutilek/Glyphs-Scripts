# MenuTitle: Report Nested Components
from GlyphsApp import Glyphs


flatten = False

for g in Glyphs.font.glyphs:
	if not g.export:
		continue

	for l in g.layers:
		for c in l.components:
			base = c.component.layers[l.layerId]
			if hasattr(base, "components"):
				if base.components and not base.paths:
					if not flatten:
						print(f"Nested component: {c.componentName} in glyph {g.name}")
					if flatten:
						if l.anchors:
							print(f"Anchors existed in {g.name}, please fix manually")
							continue

						for cc in l.components:
							cc.automaticAlignment = False
						c.decompose()
