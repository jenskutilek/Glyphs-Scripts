# MenuTitle: Activate Corretto

from jkFontTools.corretto import Corretto

def exportCallback(info):
        try:
                font_path = info.object()
                print "Fixing font with Corretto ..."
                c = Corretto(font_path, debug=False)
                if "fpgm" in c.font:
                        unhinted = False
                else:
                        unhinted = True
                c.optimizeTTGlyphs(optimizeForUnhinted=unhinted, vHintsOnly=True, noGlyphnames=False, dont_round_glyphs=[], overlap_glyphs=[])
                c.save(font_path)
                print "OK."
        except:
                # Error. Print exception.
                import traceback
                print traceback.format_exc()

Glyphs.addCallback(exportCallback, DOCUMENTEXPORTED)
