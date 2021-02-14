# MenuTitle: Rename TT Stems
stem_names = (
    "Y0: 167",
    "Y1: 156",
    "Y2: 143",
    "Y3: 123",
    "Y4: 109",
    "Y5: 184",
    "Y6: 084",
)

for m in Glyphs.font.masters:
    for i, stem in enumerate(m.customParameters["TTFStems"]):
        stem.setName_(stem_names[i])
