# MenuTitle: Assign Auto TT Stems

__doc__ = """
Assign any "auto" TT stems in selected layers to the closest stem. Stems are
taken from the master's custom parameter "TTStems".
"""

font = Glyphs.font
font.disableUpdateInterface()

for layer in font.selectedLayers:
    for hint in layer.hints:
        if hint.type == TTSTEM:
            if hint.stem == -1:
                continue
            print(hint.stem)
            if hint.horizontal:
                dist = abs(
                    hint.originNode.position.y - hint.targetNode.position.y
                )
                dists = {
                    abs(dist - s.width()): i
                    for i, s in enumerate(
                        layer.master.customParameters["TTFStems"]
                    )
                    if s.horizontal()
                }
            else:
                dist = abs(
                    hint.originNode.position.x - hint.targetNode.position.x
                )
                dists = {
                    abs(dist - s.width()): i
                    for i, s in enumerate(
                        layer.master.customParameters["TTFStems"]
                    )
                    if not s.horizontal()
                }
            min_value = sorted(dists.keys())[0]
            hint.stem = dists[min_value]

font.enableUpdateInterface()
