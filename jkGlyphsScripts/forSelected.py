from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from GlyphsApp import GSFont


def forAllLayersOfSelectedGlyphs(font: GSFont, call_function: Callable) -> None:
    for selected_layer in font.selectedLayers:
        glyph = selected_layer.parent
        for layer in glyph.layers:
            call_function(layer)
