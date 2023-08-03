# MenuTitle: Apply UFO PS Hints
from __future__ import annotations

from GlyphsApp import BOTTOMGHOST, OFFCURVE, TOPGHOST, Glyphs, GSHint

hintkey = "com.adobe.type.autohint.v2"


def findNodeWithCoordinate(layer, pos, dist_direction=0, compare_pos=0, tolerance=1):
    # dist_direction 0 = vstem, we are looking for an x coordinate
    # dist_direction 1 = hstem, we are looking for a y coordinate
    # compare_pos is the secondary coordinate that will be compared to the current
    # node's secondary coordinate in order to find the closest matching node
    candidates = []
    for p in layer.paths:
        for n in p.nodes:
            if n.type == OFFCURVE:
                continue
            diff = abs(pos - n.position[dist_direction])
            secondary_diff = abs(n.position[not dist_direction] - compare_pos)
            if diff <= tolerance:
                candidates.append((diff, secondary_diff, n))
    if candidates:
        candidates.sort(key=lambda d: (d[1], d[0]))
        # print "Candidates for", pos, compare_pos
        # for c in candidates:
        # 	print "   ", c
        diff, _, n = candidates[0]
        return n
    else:
        return None


def getHint(
    layer,
    dist_direction,
    pos,
    width,
    point_snap_tolerance=0,
):
    if dist_direction == 1 and width in (-20, -21):
        pos = pos + width

    originNode = findNodeWithCoordinate(
        layer,
        pos,
        dist_direction,
        compare_pos=0,
        tolerance=point_snap_tolerance,
    )
    if originNode is None:
        return None

    if dist_direction == 1 and width in (-20, -21):
        # This is a ghost hint
        newHint = GSHint()
        if width == -20:
            newHint.type = TOPGHOST
        else:
            newHint.type = BOTTOMGHOST

        newHint.originNode = originNode
        newHint.horizontal = dist_direction
    else:
        origin_coords = originNode.position
        targetNode = findNodeWithCoordinate(
            layer,
            pos + width,
            dist_direction,
            compare_pos=origin_coords[not dist_direction],
            tolerance=point_snap_tolerance,
        )
        if targetNode is None:
            return None

        newHint = GSHint()
        newHint.originNode = originNode
        newHint.targetNode = targetNode
        newHint.horizontal = dist_direction

    return newHint


def applyHintsToLayer(layer, point_snap_tolerance=0):

    # Clear the current Glyphs hints
    layer.hints = []

    # Read data from the Adobe V2 hinting from the UFO lib
    data = layer.userData.get(hintkey)
    if data is None:
        return None

    # Parse the data
    seen_hints = []
    for hintset in data.get("hintSetList", []):
        for stem in hintset.get("stems", []):
            stemlist = stem.split(" ")
            if len(stemlist) != 3:
                print(
                    f"Unrecognized stem format in glyph /{layer.parent.name}: '{stem}'"
                )
                continue

            cmd, pos, width = stemlist
            if cmd == "vstem":
                hint_list = [(0, pos, width)]

            elif cmd == "hstem":
                hint_list = [(1, pos, width)]

            # elif cmd == "vstem3":
            #     values = stem.attrib["stem3List"].split(",")
            #     hint_list = [
            #         (0, values[i], values[i + 1]) for i in range(0, len(values), 2)
            #     ]

            # elif cmd == "hstem3":
            #     values = stem.attrib["stem3List"].split(",")
            #     hint_list = [
            #         (1, values[i], values[i + 1]) for i in range(0, len(values), 2)
            #     ]

            else:
                print(
                    f"Unknown element '{cmd}' in hintset of glyph {layer.parent.name}."
                )
                print(data)
                continue

            for dist_direction, pos, width in hint_list:
                hint = getHint(
                    layer,
                    dist_direction,
                    float(pos),
                    float(width),
                    point_snap_tolerance,
                )
                if hint is not None:
                    if (dist_direction, pos, width) not in seen_hints:
                        layer.hints.append(hint)
                        seen_hints.append((dist_direction, pos, width))
                    # else skip hint from a different hint set with the same direction,
                    # position and width
                else:
                    print(
                        f"No suitable points to attach {cmd} at "
                        f"{'xy'[dist_direction]} = {pos}, width {width} in glyph "
                        f"/{layer.parent.name} could be found."
                    )


for layer in Glyphs.font.selectedLayers:
    applyHintsToLayer(layer, point_snap_tolerance=0)
