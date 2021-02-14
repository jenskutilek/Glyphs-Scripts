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
            o_idx = hint.originIndex()
            t_idx = hint.targetIndex()
            o_node = layer.paths[o_idx[0]].nodes[o_idx[1]]
            t_node = layer.paths[t_idx[0]].nodes[t_idx[1]]
            print(o_node, t_node)
            if hint.horizontal:
                dist = abs(o_node.y - t_node.y)
                dists = {
                    abs(dist - s.width()): i
                    for i, s in enumerate(
                        layer.master.customParameters["TTFStems"]
                    )
                    if s.horizontal()
                }
            else:
                dist = abs(o_node.x - t_node.x)
                dists = {
                    abs(dist - s.width()): i
                    for i, s in enumerate(
                        layer.master.customParameters["TTFStems"]
                    )
                    if not s.horizontal()
                }
            print("Choosing", dist, "from", dists)
            min_value = sorted(dists.keys())[0]
            if min_value < 20:
                hint.stem = dists[min_value]
            else:
                print(
                    "Could not find a matching stem for distance",
                    dist,
                    "in",
                    dists,
                )
                print("Nodes:", o_node, t_node)

font.enableUpdateInterface()
