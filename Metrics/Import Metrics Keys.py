# MenuTitle: Import Metrics Keys

from jkGlyphsHelpers.file.yaml import load_from_yaml
from jkGlyphsHelpers.forAll import forAllGlyphs
from jkGlyphsHelpers.ui.dialogs import AskYesNoCancel

__doc__ = """
Import metrics keys from a YAML file.
"""


def apply_metrics_key(glyph, metrics_keys, clear):
    if clear:
        if glyph.leftMetricsKey:
            glyph.leftMetricsKey = None
        if glyph.rightMetricsKey:
            glyph.rightMetricsKey = None
        if glyph.widthMetricsKey:
            glyph.widthMetricsKey = None
    if glyph_keys := metrics_keys.get(glyph.name):
        if left := glyph_keys.get("LSB"):
            glyph.leftMetricsKey = left
        if right := glyph_keys.get("RSB"):
            glyph.rightMetricsKey = right
        if width := glyph_keys.get("wdt"):
            glyph.widthMetricsKey = width


d = load_from_yaml()

if metrics_keys := d.get("metricsKeys"):
    clear = AskYesNoCancel(
        "Clear existing metrics keys?",
        informativeText=(
            "Do you want to clear any existing metrics keys before applying the metrics"
            " keys imported from the file?"
        ),
    )
    forAllGlyphs(apply_metrics_key, metrics_keys=metrics_keys, clear=clear)
