# MenuTitle: Export All Fonts
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

path = GetFolder(
    message="Select Destination Folder", allowsMultipleSelection=False
)

if path is None:
    print("No folder was selected; aborting.")
else:
    for font in Glyphs.fonts:
        for inst in font.instances:
            if not inst.active:
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
