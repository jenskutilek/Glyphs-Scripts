# MenuTitle: Show Index Of Selected Nodes
from __future__ import print_function

print(Glyphs.font.selectedLayers[0].glyph.name)

for path_index, path in enumerate(Glyphs.font.selectedLayers[0].paths):
    for node_index, node in enumerate(path.nodes):
        if node.selected:
            print(path_index, node_index)
