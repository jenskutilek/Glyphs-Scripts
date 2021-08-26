# MenuTitle: Align Components With Background

l = Glyphs.font.selectedLayers[0]
for c in l.components:
    if c.automaticAlignment:
        continue
    cbox = c.bounds
    for p in l.background.paths:
        pbox = p.bounds
        if (
            cbox.size.width == pbox.size.width
            and cbox.size.height == pbox.size.height
        ):
            if (
                cbox.origin.x != pbox.origin.x
                or cbox.origin.y != pbox.origin.y
            ):
                c.position = (
                    c.position.x + pbox.origin.x - cbox.origin.x,
                    c.position.y + pbox.origin.y - cbox.origin.y,
                )
