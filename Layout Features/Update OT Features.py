# MenuTitle: Update OT Features With Extra Code
# coding: utf-8
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

__doc__ = """
Reads additional OpenType layout feature code from the glyphs’ userdata and
appends it to automatically generated features.
"""

# Set user data like this:
# Font.glyphs["j_acutecomb"].userData[userdata_key] = {"locl": "script latn;\nlanguage NLD;\nsub iacute j' by j_acutecomb; # Dutch jacute"}
# Font.glyphs["J_acutecomb"].userData[userdata_key] = {"locl": "script latn;\nlanguage NLD;\nsub Iacute J' by J_acutecomb; # Dutch Jacute"}

userdata_key = "de.kutilek.otlfc"

keywords = ["sub", "pos", "by"]


def cleanup_code(code):
    # Remove comments and reformat lines to end with ;
    long = ""
    lines = code.splitlines()
    for line in lines:
        line = line.strip()
        code_comments = line.split("#", 1)
        code = code_comments[0].strip()
        long += code
    # return long
    new_lines = long.split(";")
    new_lines = ";\n".join(new_lines)
    new_lines = new_lines.split("{")
    new_lines = "{\n".join(new_lines)
    # print new_lines
    return new_lines.splitlines()


def extract_glyph_names(code):
    # for substitution only!
    names = [
        n.strip("[']")
        for n in code.strip(";").split()
        if n not in keywords and not n.startswith("@")
    ]
    # TODO: positioning
    return names


def collect_feature_code(font):
    all_glyph_names = [g.name for g in font.glyphs if g.export]
    features = {}
    for g in [glyph for glyph in font.glyphs if glyph.export]:
        data = g.userData[userdata_key]
        if data is None:
            continue
        # "DFLT": "dflt"
        current_script = "DFLT"
        current_lang = "dflt"
        for tag, code in data.items():
            code = cleanup_code(code)
            for line in code:
                if line.startswith("script"):
                    _, s = line.strip(";").split()
                    current_script = s
                elif line.startswith("language"):
                    _, l = line.strip(";").split()
                    current_language = l
                else:
                    glyph_names = extract_glyph_names(line)
                    if all([n in all_glyph_names for n in glyph_names]):
                        if tag not in features:
                            features[tag] = {
                                current_script: {current_language: [line]}
                            }
                        else:
                            if current_script not in features[tag]:
                                features[tag][current_script] = {
                                    current_language: [line]
                                }
                            else:
                                if (
                                    current_language
                                    not in features[tag][current_script]
                                ):
                                    features[tag][current_script][
                                        current_language
                                    ] = [line]
                                else:
                                    features[tag][current_script][
                                        current_language
                                    ].append(line)
    print(features)
    return features


def get_feature_code(code_dict):
    # Return FDK syntax feature code
    current_script = "DFLT"
    current_lang = "dflt"
    result = ""
    indent = 0
    for s, d0 in code_dict.items():
        if s != current_script:
            indent = max(indent - 4, 0)
            result += " " * indent + "script %s;\n" % s
            current_script = s
            indent += 8
        for l, d1 in d0.items():
            if l != current_lang:
                indent = max(indent - 4, 0)
                result += " " * indent + "language %s;\n" % l
                current_lang = l
                indent += 4
            for c in d1:
                result += " " * indent + "%s\n" % c
    return result


def apply_features(font, feature_dict):
    existing_tags = [f.name for f in font.features]
    for tag, code in feature_dict.items():
        if tag not in existing_tags:
            font.features.append(GSFeature(tag, get_feature_code(code)))
        else:
            for fea in font.features:
                if not fea.automatic:
                    continue
                fea.update()
                if tag == fea.name:
                    fea.code += get_feature_code(code)
                    # print get_feature_code(code)
                    print("*** %s is now:" % tag)
                    print(fea.code)
                    break


f = collect_feature_code(Font)
apply_features(Font, f)
