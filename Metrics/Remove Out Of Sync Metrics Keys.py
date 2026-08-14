# MenuTitle: Remove Out Of Sync Metrics Keys

from GlyphsApp import Glyphs

for glyph in Glyphs.font.glyphs:
    for layer in glyph.layers:
        lsb = layer.LSB
        layer.syncLeftMetrics()
        if lsb != layer.LSB:
            print(
                f"{glyph.name}: Actual LSB {lsb} vs. key {layer.LSB}. Removing left key {glyph.leftMetricsKey}"
            )
            layer.LSB = lsb
            glyph.leftMetricsKey = None
        rsb = layer.RSB
        layer.syncRightMetrics()
        if rsb != layer.RSB:
            print(
                f"{glyph.name}: Actual RSB {rsb} vs. key {layer.RSB}. Removing right key {glyph.rightMetricsKey}"
            )
            layer.RSB = rsb
            glyph.rightMetricsKey = None
