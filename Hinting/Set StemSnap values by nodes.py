# MenuTitle: Set StemSnap values by reference nodes
from __future__ import print_function

ref_distances = [
    # Glyph name, path index, node index, path.index, node index
    # 167
    ("o", (0, 5), (1, 5)),
    # 156
    ("e.ss01", (0, 6), (0, 30)),
    # ("e", (0, 6), (0, 31)), # Italic
    # 143
    ("e.ss01", (0, 12), (0, 24)),
    # ("e", (0, 12), (0, 25)), # Italic
    # 123
    ("a.text", (0, 30), (1, 11)),
    # ("eight.dnom", (0, 36), (0, 49)), # Italic
    # 109
    ("e.ss01", (0, 15), (0, 18)),
    # ("e", (0, 18), (0, 19)), # Italic
    # 184
    ("O", (0, 5), (1, 5)),
    # 84
    ("published", (0, 5), (1, 5)),
]

stems = {m.id: [] for m in Glyphs.font.masters}

for glyph_name, start_node, end_node in ref_distances:
    # print("\n", glyph_name, start_node, end_node)
    glyph = Glyphs.font.glyphs[glyph_name]
    start_path_index, start_node_index = start_node
    end_path_index, end_node_index = end_node
    for layer in glyph.layers:
        if layer.master is None:
            continue
        # print(glyph_name, layer.master.name)
        start = layer.paths[start_path_index].nodes[start_node_index]
        end = layer.paths[end_path_index].nodes[end_node_index]
        value = int(round(abs(end.position.y - start.position.y)))
        # print("   ", start, end, value)
        stems[layer.master.id].append(value)

for m in Glyphs.font.masters:
    print(m)
    if m.id in stems:
        if m.horizontalStems != stems[m.id]:
            m.horizontalStems = stems[m.id]
            print("  Old:", m.horizontalStems)
            print("  New:", m.horizontalStems)
        print("  Unchanged.")
    else:
        print("Master not found:", m.id, m)


# 200,190,212,181,145,156,99
# 167,156,143,123,109,184,84
