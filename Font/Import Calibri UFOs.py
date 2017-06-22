#MenuTitle: Import Calibri UFOs

import os
from os.path import join

font_version = 25

ufos = [
    ("CalibriMMvarPS-MiniSubset%s.ufo" % font_version,   "Thin Cd",        (   0,  50, 11), (-1, -1,  0)),
    ("CalibriMMvarPS-MiniSubset%s-1.ufo" % font_version, "Reg Cd",         (1000,  50, 11), ( 0, -1,  0)),
    ("CalibriMMvarPS-MiniSubset%s-2.ufo" % font_version, "Black Cd",       (2000,  50, 11), ( 1, -1,  0)),
    ("CalibriMMvarPS-MiniSubset%s-3.ufo" % font_version, "Thin",           (   0, 100, 11), (-1,  0,  0)),
    ("CalibriMMvarPS-MiniSubset%s-4.ufo" % font_version, "Reg",            (1000, 100, 11), ( 0,  0,  0)),
    ("CalibriMMvarPS-MiniSubset%s-5.ufo" % font_version, "Reg Optical",    (1000, 100,  6), ( 0,  0, -1)),
    ("CalibriMMvarPS-MiniSubset%s-6.ufo" % font_version, "Black",          (2000, 100, 11), ( 1,  0,  0)),
    ("CalibriMMvarPS-MiniSubset%s-7.ufo" % font_version, "Thin Extd",      (   0, 200, 11), (-1,  1,  0)),
    ("CalibriMMvarPS-MiniSubset%s-8.ufo" % font_version, "Reg Extd",       (1000, 200, 11), ( 0,  1,  0)),
    ("CalibriMMvarPS-MiniSubset%s-9.ufo" % font_version, "Black Extd",     (2000, 200, 11), ( 1,  1,  0)),
    
#    ("CalibriMMvarPS-MiniSubset%s-10.ufo" % font_version, "Old Light",     (   0, 100, 11), (-1, -1,  0)),
#    ("CalibriMMvarPS-MiniSubset%s-11.ufo" % font_version, "Old ExtraBold", (   0, 100, 11), (-1, -1,  0)),
]

weight_names = {
    0: "Light",
    1000: "Regular",
    2000: "Bold",
}

width_names = {
    50: "Condensed",
    100: "Normal",
    200: "Extended",
}

custom_names = {
    6: "Small Text",
    11: "",
}



base_path = "/Volumes/Machine/Calibri/2017/TTF Conversion cu2qu"
ref_path =  "/Volumes/Machine/Calibri/2017/TTF Conversion cu2qu/reference"

base_ufo = join(base_path, ufos[0][0][:-4] + "TT.ufo")

if os.path.exists(base_ufo):
    print "Opening ..."
    mm = Glyphs.open(base_ufo)
    
    # Add info to the base font
    
    mm.customParameters["Axes"] = [
        {"Name": "Weight",       "Tag": "wght"},
        {"Name": "Width",        "Tag": "wdth"},
        {"Name": "Optical size", "Tag": "opsz"},
    ]
    
    # Add info to the base master
    
    m0 = mm.masters[0]
    m0.weightValue, m0.widthValue, m0.customValue = ufos[0][2]
        
    m0.weight      = weight_names[ufos[0][2][0]]
    m0.width       = width_names [ufos[0][2][1]]
    m0.customName  = custom_names[ufos[0][2][2]]
    
    m0.customParameters["Axis Location"] = [
        {"Axis": "Weight",       "Location": "%s" % ufos[0][3][0]},
        {"Axis": "Width",        "Location": "%s" % ufos[0][3][1]},
        {"Axis": "Optical size", "Location": "%s" % ufos[0][3][2]},
    ]
    
    # Open corresponding PS file and put in background
    
    base_ps_ufo = join(ref_path, ufos[0][0])
    
    if os.path.exists(base_ps_ufo):
        ps = Glyphs.open(base_ps_ufo)
        for g in mm.glyphs:
            ps_layer = ps.glyphs[g.name].layers[0]
            g.layers[m0.id].background = ps_layer.copy()
        ps.close()
    
    
    for ufo, master_name, glyphs_params, vf_params in ufos[1:]:
        tt_path = join(base_path, ufo[:-4] + "TT.ufo")
        ps_path = join(ref_path, ufo)
        
        tt = Glyphs.open(tt_path)
        ps = Glyphs.open(ps_path)
        m = tt.masters[0]
        
        m.weightValue, m.widthValue, m.customValue = glyphs_params
        
        m.weight      = weight_names[glyphs_params[0]]
        m.width       = width_names [glyphs_params[1]]
        m.customName  = custom_names[glyphs_params[2]]
        
        m.customParameters["Axis Location"] = [
            {"Axis": "Weight",       "Location": "%s" % vf_params[0]},
            {"Axis": "Width",        "Location": "%s" % vf_params[1]},
            {"Axis": "Optical size", "Location": "%s" % vf_params[2]},
        ]
        
        mm.masters.append(m.copy())
        
        mid = m.id
        
        for g in mm.glyphs:
            ttl = tt.glyphs[g.name].layers[0]
            psl = ps.glyphs[g.name].layers[0]
            g.layers[mid] = ttl.copy()
            g.layers[mid].background = psl.copy()
        
        tt.close()
        ps.close()
    
    print mm
