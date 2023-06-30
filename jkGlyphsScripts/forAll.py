from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from GlyphsApp import GSFont


def forAllLayersOfAllGlyphs(font: GSFont, call_function: Callable, **kwargs) -> None:
    font.disableUpdateInterface()
    for glyph in font.glyphs:
        for layer in glyph.layers:
            call_function(layer, **kwargs)
    font.enableUpdateInterface()
