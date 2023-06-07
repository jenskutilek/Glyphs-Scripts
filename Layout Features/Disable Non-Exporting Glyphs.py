# MenuTitle: Disable Non-exporting Glyphs in Classes
__doc__="""
In all active OpenType classes, comment out glyph names that are set to
"no export". Expects classes to be formatted with one glyph name per line.
"""


def exporting(font, glyphname):
    if glyphname in font.glyphs:
        glyph = font.glyphs[glyphname]
        if glyph.export:
            return True
    return False


f = Glyphs.font

for c in f.classes:
    if not c.active:
        continue
    glyphs = c.code.splitlines()
    active_glyphs = []
    for name in glyphs:
        if not name:
            continue

        name = name.strip()
        if name.startswith("#NOEXPORT:"):
            name = name[10:]
            if not name:
                continue

            if exporting(f, name):
                active_glyphs.append(name)
            else:
                active_glyphs.append("#NOEXPORT:%s" % name)
        elif name.startswith("#"):
            active_glyphs.append(name)
        else:
            if exporting(f, name):
                active_glyphs.append(name)
            else:
                active_glyphs.append("#NOEXPORT:%s" % name)

    c.code = "\n".join(active_glyphs)
