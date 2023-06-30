# MenuTitle: Export All Fonts
from GlyphsApp import GetFolder, Glyphs

path = GetFolder(message="Select Destination Folder", allowsMultipleSelection=False)

if path is None:
    print("No folder was selected; aborting.")
else:
    for font in Glyphs.fonts:
        for inst in font.instances:
            if not inst.exports:
                continue

            inst.generate(
                Format="OTF",
                FontPath=path,
                AutoHint=False,
                RemoveOverlap=False,
                UseSubroutines=True,
                UseProductionNames=True,
                # Containers="plain",
            )
