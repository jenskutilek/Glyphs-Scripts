# MenuTitle: Activate Corretto

import os
from fontTools.ttLib import TTFont
from jkFontTools.corretto import Corretto

def exportCallback(info):
    try:
        font_path = info.object()
        if font_path.endswith(".ttf"):
            print "Fixing font with Corretto ..."
            c = Corretto(font_path, debug=False)
            if "fpgm" in c.font:
                unhinted = False
            else:
                unhinted = True
            c.optimizeTTGlyphs(optimizeForUnhinted=unhinted, vHintsOnly=True, noGlyphnames=False, dont_round_glyphs=[], overlap_glyphs=[])
            c.save(font_path)
            print "OK."
        elif font_path.endswith(".otf"):
            print "Postprocessing OTF font ..."
            f = TTFont(font_path)
            head, tail = os.path.split(font_path)
            head, _ = os.path.split(head)
            xml_dir = os.path.join(head, "otf_ttx")
            if not os.path.exists(xml_dir):
                os.mkdir(xml_dir)
            if os.path.isdir(xml_dir):
                xml_path = os.path.join(xml_dir, "%s.xml" % tail.splitext()[0])
                print "    Saving TTX dump to:", xml_path
                f.saveXML(xml_path)
                print "OK."
            else:
                print "Error writing to folder '%s'." % xml_dir
    except:
        # Error. Print exception.
        import traceback
        print traceback.format_exc()

Glyphs.addCallback(exportCallback, DOCUMENTEXPORTED)
