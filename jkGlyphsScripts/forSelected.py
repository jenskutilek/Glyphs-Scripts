from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from GlyphsApp import GSFont


def forAllLayersOfSelectedGlyphs(
    font: GSFont, call_function: Callable, **kwargs
) -> None:
    font.disableUpdateInterface()
    for selected_layer in font.selectedLayers:
        glyph = selected_layer.parent
        for layer in glyph.layers:
            call_function(layer, **kwargs)
    font.enableUpdateInterface()


def forSelectedLayers(font: GSFont, call_function: Callable, **kwargs) -> None:
    font.disableUpdateInterface()
    for selected_layer in font.selectedLayers:
        call_function(selected_layer, **kwargs)
    font.enableUpdateInterface()
