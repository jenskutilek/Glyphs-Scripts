# MenuTitle: Remove Duplicate Nodes
from GlyphsApp import Glyphs

for layer in Glyphs.font.selectedLayers:
    for path in layer.paths:
        remove_nodes = []
        for i, node in enumerate(path.nodes):
            if node.prevNode.x == node.x and node.prevNode.y == node.y:
                remove_nodes.append(i)
        for i in reversed(remove_nodes):
            del path.nodes[i]
