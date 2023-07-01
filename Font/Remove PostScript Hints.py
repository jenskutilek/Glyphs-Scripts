# MenuTitle: Remove PostScript Hints

from GlyphsApp import TOPGHOST, STEM, BOTTOMGHOST
from jkGlyphsHelpers.forAll import forAllLayersOfAllGlyphs

__doc__ = """
Remove PostScript hints in all glyphs of the current font
"""

ps_hints = [
    TOPGHOST,
    STEM,
    BOTTOMGHOST,
]


def remove_hints(layer):
    delete = []
    for i, hint in enumerate(layer.hints):
        if hint.isPostScript and hint.type in ps_hints:
            delete.append(i)
    if delete:
        for i in reversed(delete):
            del layer.hints[i]


forAllLayersOfAllGlyphs(remove_hints)
