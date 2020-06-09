# MenuTitle: FontForge (SFD) Import
from __future__ import absolute_import, division, print_function, unicode_literals
import codecs

header_font_map = {
	"Copyright": "copyright",
	"FamilyName": "familyName",
	"UComments": "note",
}

header_master_map = {
	"Ascent": "ascender",
	"Descent": "descender",
	"ItalicAngle": "italicAngle",
}

header_instance_map = {
	"FontName": "fontName",
	"Weight": "weight",
}


def to_num(s):
	if "." in s:
		return float(s)
	return int(s)


class SFDImport(object):
	def __init__(self, sfd_path):
		self.sfd_path = sfd_path
		self.read_sfd()
		self.import_sfd()

	def read_sfd(self):
		with codecs.open(self.sfd_path, "rb", encoding="utf-7") as f:
			self.sfd = f.read()

	def get_parts(self):
		"""Get header and glyph data parts"""
		header, chars = self.sfd.split("BeginChars:", 1)
		return header, chars

	def import_sfd(self):
		self.font = GSFont()
		self.font.disablesNiceNames = True
		self.font.disablesAutomaticAlignment = True
		self.font.show()
		self.font.disableUpdateInterface()
		self.master = self.font.masters[0]
		self.font.instances.append(GSInstance())
		self.instance = self.font.instances[0]
		header, chars = self.get_parts()
		self.import_header(header)
		self.import_glyphs(chars)
		self.font.enableUpdateInterface()

	def import_header(self, header):
		assert header.startswith("SplineFontDB:")
		in_private = False
		for line in header.splitlines():
			k_v = line.split(":")
			if len(k_v) == 2:
				k, v = k_v
				k = k.strip()
				v = v.strip()
				if k == "BeginPrivate":
					print("BeginPrivate")
					in_private = True
				elif k == "EndPrivate":
					in_private = False
				elif k in header_font_map:
					setattr(self.font, header_font_map[k], v)
				elif k in header_instance_map:
					setattr(self.instance, header_instance_map[k], v)
				elif k in header_master_map:
					if k == "Descent":
						self.master.descender = -1 * to_num(v)
					else:
						setattr(self.master, header_master_map[k], to_num(v))
			elif in_private:
				if line.startswith("EndPrivate"):
					continue

				k, n, v = line.split(" ", 2)
				if k == "BlueValues":
					blueValues = [
						to_num(i.strip("[]"))
						for i in v.split()
					]
					print(blueValues)
					self.master.alignmentZones = [
						GSAlignmentZone(blueValues[i], blueValues[i + 1] - blueValues[i])
						for i in range(0, len(blueValues), 2)
					]
				elif k == "StdHW":
					self.master.horizontalStems = [to_num(v.strip("[]"))]
				elif k == "StemSnapH":
					self.master.horizontalStems = [
						self.master.horizontalStems[0]
					] + [
						to_num(i.strip("[]"))
						for i in v.split()
					]
				elif k == "StdVW":
					self.master.verticalStems = [to_num(v.strip("[]"))]
				elif k == "StemSnapV":
					self.master.verticalStems = [
						self.master.verticalStems[0]
					] + [
						to_num(i.strip("[]"))
						for i in v.split()
					]
				else:
					pass

	def import_glyphs(self, glyphs):
		glyph = None
		glyphOrder = {}
		in_splineSet = False
		path = False
		for line in glyphs.splitlines():
			# print(">>>> %s >>>>" % line)
			if line.startswith("StartChar:"):
				# print("StartChar")
				in_splineSet = False
				_, name = line.split(":")
				name = name.strip()
				# print(name)
				glyph = GSGlyph(name)
				self.font.glyphs.append(glyph)
				name = glyph.name
				glyph = self.font.glyphs[name]
				layer = glyph.layers[0]
			elif line.strip() == "EndChar":
				# print("EndChar")
				glyph = None
				layer = None
			elif line.startswith("Encoding:"):
				_, enc, uenc, gid = line.split()
				glyph.unicode = "%04X" % int(enc)
				glyphOrder[int(gid)] = name
			elif line.startswith("Width:"):
				_, w = line.split()
				layer.width = to_num(w)
			elif line.startswith("Fore"):
				cur_layer = "Fore"
			elif line.startswith("SplineSet"):
				in_splineSet = True
				pen = layer.getPen()
			elif line.startswith("EndSplineSet"):
				in_splineSet = False
				if path:
					pen.closePath()
				path = False
			elif in_splineSet:
				parts = line.split()
				seg_type = parts[-2]
				if seg_type == "m":
					if path:
						pen.closePath()
					path = True
					x, y = parts[:2]
					pen.moveTo((to_num(x), to_num(y)))
				elif seg_type == "l":
					x, y = parts[:2]
					pen.lineTo((to_num(x), to_num(y)))
				elif seg_type == "c":
					x0, y0, x1, y1, x, y, _, _ = parts
					pen.curveTo(
						(to_num(x0), to_num(y0)),
						(to_num(x1), to_num(y1)),
						(to_num(x), to_num(y))
					)
			else:
				pass
				# print("Unhandled data:", line)


sfd = SFDImport("/Users/kuti/Downloads/salieri-regular.sfd")
print("OK.")
