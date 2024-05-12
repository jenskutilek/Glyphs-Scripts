# MenuTitle: Set Up Smart Components For Selected Layers

from copy import copy
from GlyphsApp import Glyphs, GSSmartComponentAxis

font = Glyphs.font

for layer in font.selectedLayers:
    glyph = layer.parent
    # try:
    # 	glyph.smartComponentAxes["Cap"]
    # except:
    # 	continue

    print(f"Adding axis to glyph {glyph.name}")

    axis = GSSmartComponentAxis()
    axis.topValue = 644
    axis.bottomValue = 458
    axis.name = "Cap"
    glyph.smartComponentAxes.append(axis)
    smartAxis = glyph.smartComponentAxes["Cap"]

    source_name = glyph.name.split(".")[-1]
    for master in font.masters:
        main_layer = glyph.layers[master.id]
        main_layer.clear()
        source_layer = copy(font.glyphs[source_name].layers[master.id])
        print(
            f"Copying width for layer {main_layer.name} from {source_name}: {source_layer.width}"
        )
        for path in source_layer.paths:
            main_layer.paths.append(path)
        for anchor in source_layer.anchors:
            main_layer.anchors.append(anchor)
        main_layer.width = source_layer.width
        main_layer.smartComponentPoleMapping[smartAxis.id] = 2

        pcap_source_name = f"{source_name.lower()}.pcap"
        source_layer = font.glyphs[pcap_source_name].layers[master.id]
        pcap_layer = copy(source_layer)
        glyph.layers.append(pcap_layer)
        pcap_layer.name = f"{main_layer.name} pcap"
        pcap_layer.associatedMasterId = master.id
        pcap_layer.smartComponentPoleMapping[smartAxis.id] = 1
        pcap_layer.width = source_layer.width
