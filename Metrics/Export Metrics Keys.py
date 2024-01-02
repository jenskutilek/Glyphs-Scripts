# MenuTitle: Export Metrics Keys

from GlyphsApp import Glyphs
from jkGlyphsHelpers.file.yaml import save_as_yaml

__doc__ = """
Export a YAML file that contains the current font’s metrics keys.
"""


metrics_keys = {"metricsKeys": {}}
d = metrics_keys["metricsKeys"]


for glyph in Glyphs.font.glyphs:
    name = str(glyph.name)
    if glyph.leftMetricsKey:
        if name not in d:
            d[name] = {}
        d[name]["LSB"] = str(glyph.leftMetricsKey)
    if glyph.widthMetricsKey:
        if name not in d:
            d[name] = {}
        d[name]["wdt"] = str(glyph.widthMetricsKey)
    if glyph.rightMetricsKey:
        if name not in d:
            d[name] = {}
        d[name]["RSB"] = str(glyph.rightMetricsKey)

save_as_yaml(
    metrics_keys, ProposedFileName=f"{Glyphs.font.familyName}.metricsKeys.yaml"
)
