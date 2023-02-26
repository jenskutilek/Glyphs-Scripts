# MenuTitle: Show Generated GPOS Code
__doc__="""
Compile a feature file for GPOS features, as Glyphs does on export, and print it
"""

from Foundation import NSClassFromString, NSString, NSTemporaryDirectory
from GlyphsApp import Glyphs, GSOutlineFormatTrueType
font = Glyphs.font
instance = font.instances[0]
exportInstanceOperation = NSClassFromString("GSExportInstanceOperation").alloc().initWithFont_instance_outlineFormat_containers_(font, instance, GSOutlineFormatTrueType, None)

tempFile = NSTemporaryDirectory().stringByAppendingPathComponent_("feature.fea")

result = exportInstanceOperation.writeFeaFile_error_(tempFile, None)
# print(result)

feaCode = NSString.stringWithContentsOfFile_(tempFile)
print(feaCode)
