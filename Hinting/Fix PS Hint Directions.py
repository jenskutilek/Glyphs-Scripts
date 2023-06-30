# MenuTitle: Fix PS Hint Directions
from GlyphsApp import Glyphs
from jkGlyphsScripts.forAll import forAllLayersOfAllGlyphs
from jkGlyphsScripts.hintingPS.ocd import fix_hint_directions


forAllLayersOfAllGlyphs(Glyphs.font, fix_hint_directions)
