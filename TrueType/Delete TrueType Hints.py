# MenuTitle: Delete TrueType Hints In Selected Layers
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from GlyphsApp import (
    Glyphs,
    # Hint types
    # TTSNAP,  # See below
    TTSTEM,
    # TTSHIFT,  # See below
    TTINTERPOLATE,
    TTDIAGONAL,
    TTDELTA,
)

# Changes in Glyphs 3
try:
    # G3
    from GlyphsApp import TTSNAP, TTSHIFT
except ImportError:
    # G2
    from GlyphsApp import TTANCHOR as TTSNAP
    from GlyphsApp import TTALIGN as TTSHIFT

__doc__ = """
Remove TrueType hints in selected layers.
"""

tt_hint_types = (
    TTSNAP,
    TTSTEM,
    TTSHIFT,
    TTINTERPOLATE,
    TTDIAGONAL,
    TTDELTA,
)

font = Glyphs.font
font.disableUpdateInterface()

for layer in font.selectedLayers:
    delete = []
    for i, hint in enumerate(layer.hints):
        if hint.type in tt_hint_types:
            delete.append(i)
    if delete:
        print(layer.parent.name)
    for i in reversed(delete):
        del layer.hints[i]

font.enableUpdateInterface()
