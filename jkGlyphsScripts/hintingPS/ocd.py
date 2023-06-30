from __future__ import annotations
from GlyphsApp import GSNode, BOTTOMGHOST, TOPGHOST
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from GlyphsApp import GSLayer


def fix_hint_directions(layer: GSLayer) -> None:
    """
    Glyphs shows some PostScript hint directions as negative. This is fixed at export,
    but some people are bothered by it.
    """
    for hint in layer.hints:
        if not hint.isPostScript:
            continue

        if hint.type in (BOTTOMGHOST, TOPGHOST):
            continue

        if hint.originNode is None:
            print(f"originNode is None in {layer.parent.name}")
            continue

        if hint.targetNode is None:
            print(f"targetNode is None in {layer.parent.name}")
            continue

        if isinstance(hint.originNode, GSNode):
            if isinstance(hint.targetNode, GSNode):
                if hint.horizontal:
                    width = hint.targetNode.position.y - hint.originNode.position.y
                else:
                    width = hint.targetNode.position.x - hint.originNode.position.x

                if width < 0:
                    hint.targetNode, hint.originNode = hint.originNode, hint.targetNode
                    print(f"Switched hint nodes in {layer.parent.name}")

            else:
                print(
                    f"targetNode is not GSNode in {layer.parent.name}: "
                    f"{hint.targetNode}, ({type(hint.targetNode)})"
                )
        else:
            print(
                f"originNode is not GSNode in {layer.parent.name}: "
                f"{hint.originNode}, ({type(hint.originNode)})"
            )
