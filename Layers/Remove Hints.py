# MenuTitle: Remove Hints
from GlyphsApp import TOPGHOST, STEM, BOTTOMGHOST
from jkGlyphsHelpers.forSelected import forSelectedLayers


__doc__ = """
Remove PostScript hints in selected layers.
"""

ps_hints = [
    TOPGHOST,
    STEM,
    BOTTOMGHOST,
]


def remove_postscript_hints(layer):
    delete = []
    for i, hint in enumerate(layer.hints):
        if hint.isPostScript and hint.type in ps_hints:
            delete.append(i)
    if delete:
        for i in reversed(delete):
            del layer.hints[i]


forSelectedLayers(remove_postscript_hints)
