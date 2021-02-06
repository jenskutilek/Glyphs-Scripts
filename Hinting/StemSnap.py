# MenuTitle: Calculate StemSnap values
from __future__ import division, print_function
from fontTools.pens.basePen import BasePen

DEBUG = False


def mean(data_list):
    s = 0
    for e in data_list:
        s += e
    n = len(data_list)
    if n == 0:
        return None
    return s / len(data_list)


def median(data_list):
    n = len(data_list)
    half = n // 2
    # print "Median", data_list, "=",
    if n == 1:
        # print data_list[0]
        return data_list[0]
    if len(data_list) % 2:
        m = data_list[half]
        # print m
        return int(m)
    else:
        # m = mean([data_list[half-1], data_list[half]])
        # "low median"
        m = min([data_list[half - 1], data_list[half]])
        # print m
        return int(m)


def mode(data_list):
    d = {}
    for elm in data_list:
        try:
            d[elm] += 1
        except (KeyError):
            d[elm] = 1

    keys = d.keys()
    max = d[keys[0]]

    for key in keys[1:]:
        if d[key] > max:
            max = d[key]

    max_k = []
    for key in keys:
        if d[key] == max:
            max_k.append(key),
    return max_k, max


class StemDirectionHistogram(object):
    def __init__(self, cluster_gap=6):
        self.cluster_gap = cluster_gap
        self.num_glyphs = 0
        self.stems = []

    def add_value(self, value):
        self.stems.append(value)

    def get_group_stem_values(self):
        stems = sorted(self.stems)
        maxgap = self.cluster_gap
        # print stems
        if len(stems) > 0:
            groups = [[stems[0]]]
            for x in stems[1:]:
                # if abs(x - groups[-1][-1]) <= maxgap:
                if abs(x - mean(groups[-1])) <= maxgap:
                    groups[-1].append(x)
                else:
                    groups.append([x])
        else:
            groups = []
        return groups

    def get_values(self, limit):
        # print "get_values"
        stem_groups = self.get_group_stem_values()
        # print "stem_groups", stem_groups
        stems = {}
        for stem_group in stem_groups:
            # use the median
            # stems[int(round(median(stem_group)))] = len(stem_group)
            # or use the median of the mode
            stems[int(round(median(mode(stem_group)[0])))] = len(stem_group)

        # make a reverse map frequency -> stem widths
        rev_dict = {}
        for width, num in stems.items():
            if num in rev_dict:
                rev_dict[num].append(width)
            else:
                rev_dict[num] = [width]
        print("rev_dict", rev_dict)
        debug = ""
        for k in sorted(rev_dict.keys(), reverse=True):
            debug += "%s x %s, " % (rev_dict[k], k)
        print("Debug:")
        print(debug.strip(", "))
        sorted_stems = []
        for count in sorted(rev_dict.keys(), reverse=True):
            # if count > (self.num_glyphs // 5):
            sorted_stems.extend(sorted(rev_dict[count]))
        # print "sorted_stems", sorted_stems
        return sorted_stems[:limit]


class StemHistogram(object):
    def __init__(
        self,
        font,
        black_on_left=True,
        min_length_x=20,
        min_length_y=20,
        min_dist_x=25,
        min_dist_y=25,
        max_dist_x=400,
        max_dist_y=400,
        cluster_gap=2,
    ):
        self.font = font
        self.black_on_left = black_on_left

        # Minimum segment length for coordinate detection
        self.min_length_x = min_length_x
        self.min_length_y = min_length_y

        # Minimum and maximum distance for stem detection
        self.min_dist_x = min_dist_x
        self.min_dist_y = min_dist_y
        self.max_dist_x = max_dist_x
        self.max_dist_y = max_dist_y

        # Maximum gap for stem grouping
        self.cluster_gap = cluster_gap

        # Initialize two histograms, one for h distances and one for v distances
        self.hstem_histogram = StemDirectionHistogram(self.cluster_gap)
        self.vstem_histogram = StemDirectionHistogram(self.cluster_gap)

    def calculate_histogram(self):
        self.num_glyphs = 0
        for layer in self.font.selectedLayers:
            if len(layer.paths) > 0:
                x_distances, y_distances = self.find_glyph_stems(layer)
                self.num_glyphs += 1
                for d in x_distances:
                    self.hstem_histogram.add_value(d)
                for d in y_distances:
                    self.vstem_histogram.add_value(d)
        print(self.num_glyphs, "glyphs analyzed.")
        self.hstem_histogram.num_glyphs = self.num_glyphs
        self.vstem_histogram.num_glyphs = self.num_glyphs

    def find_glyph_stems(self, layer):
        # Adapted for Glyphs
        x_dists = []
        y_dists = []
        for hint in layer.hints:
            if hint.type != STEM:
                continue
            # print hint
            # print hint.originNode, hint.origin, hint.position, hint.width, type(hint.origin)
            if hint.originNode is None:
                width = abs(hint.width)
            else:
                width = abs(hint.width - hint.position)
            # print width
            width = int(round(width))
            if hint.horizontal:
                y_dists.append(width)
            else:
                x_dists.append(width)
        # print x_dists, y_dists
        return x_dists, y_dists


if __name__ == "__main__":
    interactive = False
    if interactive:
        if DEBUG:
            f = CurrentFont()

            h = StemHistogram(
                f,
                True,
                min_length_x=20,
                min_length_y=20,
                min_dist_x=25,
                min_dist_y=22,
                max_dist_x=120,
                max_dist_y=100,
                cluster_gap=7,
            )
            links = h.find_glyph_links(CurrentGlyph())
            print(links)
        else:
            OpenWindow(StemHistogramUI)
    else:
        f = Glyphs.font

        h = StemHistogram(f, cluster_gap=6)

        h.calculate_histogram()

        # print h.hstem_histogram.get_values(4)
        # print "\n", h.vstem_histogram.get_values(4)
        # print "StemSnapH", h.hstem_histogram.get_values(4)
        snaph = h.hstem_histogram.get_values(6)
        print("StemSnapV:", snaph)
        snapv = h.vstem_histogram.get_values(6)
        print("StemSnapV:", snapv)

        # f.info.postscriptStemSnapH = h.hstem_histogram.get_values(4)
        # f.info.postscriptStemSnapV = h.vstem_histogram.get_values(4)

        # print "\nValues were written to font info:"
        # print "  StemSnapH:", f.info.postscriptStemSnapH
        # print "  StemSnapV:", f.info.postscriptStemSnapV
