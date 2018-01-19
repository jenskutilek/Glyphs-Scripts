#MenuTitle: Activate Corretto
from __future__ import print_function

import os
from fontTools.ttLib import TTFont
from jkFontTools.corretto import Corretto


def save_as_ttx(font, font_path, subfolder):
    head, tail = os.path.split(font_path)
    head, _ = os.path.split(head)
    xml_dir = os.path.join(head, subfolder)
    if not os.path.exists(xml_dir):
        os.mkdir(xml_dir)
    if os.path.isdir(xml_dir):
        xml_path = os.path.join(xml_dir, "%s.ttx" % os.path.splitext(tail)[0])
        print("    Saving TTX dump to:", xml_path)
        font.saveXML(xml_path)
        print("OK.")
    else:
        print("Error writing to folder '%s'." % xml_dir)


def exportCallback(info):
    try:
        #font_path = info.object()
        font_path = info.object()["fontFilePath"]
        font_inst = info.object()["instance"]
        if font_path.endswith(".ttf"):
            print("Fixing font with Corretto ...")
            c = Corretto(font_path, debug=False)
            unhinted = "fpgm" not in c.font
            c.optimizeTTGlyphs(optimizeForUnhinted=unhinted, vHintsOnly=True, noGlyphnames=False, dont_round_glyphs=[], overlap_glyphs=[])
            c.save(font_path)

            save_as_ttx(c.font, font_path, "ttf_ttx")
            
            print("OK.")
        elif font_path.endswith(".otf"):
            print("Postprocessing OTF font ...")
            f = TTFont(font_path)

            # Set BlueFuzz because Glyphs doesn't export it.
            # It does now.

            #if "postscriptBlueFuzz" in Glyphs.font.customParameters:
            #    fuzz = Glyphs.font.customParameters["postscriptBlueFuzz"]
            #    print("    Setting BlueFuzz to %i ..." % fuzz)
            #    tcff = f["CFF "]
            #    go = tcff.getGlyphOrder() # Decompile the CFF table
            #    top_dict = tcff.cff.__dict__['topDictIndex'].items[0]
            #    #top_dict.decompileAllCharStrings(None)
            #    top_dict.Private.rawDict["BlueFuzz"] = fuzz

            #    # Open the font again
            #    f.save(font_path)
            #    f = TTFont(font_path)

            #print("    Checking StemSnap ...")
            #tcff = f["CFF "]
            #go = tcff.getGlyphOrder() # Decompile the CFF table
            #top_dict = tcff.cff.__dict__['topDictIndex'].items[0].Private.rawDict

            #changed = False
            #for main, stems in (("StdHW", "StemSnapH"), ("StdVW", "StemSnapV")):
            #    if stems in top_dict:
            #        if top_dict[main] not in top_dict[stems]:
            #            top_dict[stems].append(top_dict[main])
            #            print("        Appending missing %s entry to %s." % (main, stems))
            #            changed = True
            #        if top_dict[stems] != sorted(top_dict[stems]):
            #            top_dict[stems] = sorted(top_dict[stems])
            #            print("        Sorting %s." % stems)
            #            changed = True

            #if changed:
            #    # Open the font again
            #    f.save(font_path)
            #    f = TTFont(font_path)
            
            save_as_ttx(f, font_path, "otf_ttx")

    except:
        # Error. Print exception.
        import traceback
        print(traceback.format_exc())

Glyphs.addCallback(exportCallback, DOCUMENTEXPORTED)
print("Corretto is activated.")
