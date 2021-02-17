# MenuTitle: Export Stem Deltas as CSV
from __future__ import print_function, division, unicode_literals


class DeltaImportExport(object):
	def __init__(self, font):
		self.font = font
		self.hint_master = self.find_hint_master()
		self.build_instance_keys()
	
	def find_hint_master(self):
		"""
		Find the hinted master
		"""
		if "Get Hints From Master" in self.font.customParameters:
			hint_master_id = self.font.customParameters["Get Hints From Master"]
			hint_master = self.font.masters[hint_master_id]
		else:
			# First master
			hint_master = self.font.masters[0]

		print(hint_master)
		return hint_master
	
	def build_instance_keys(self):
		"""
		Build the instance keys that are used in the TTFStems delta dict
		"""
		self.instance_keys = {}
		# print(self.font.axes)
		for i, instance in enumerate(self.font.instances):
			# Sort axes by name to achieve the final order of axis values
			order = [
				(
					self.font.axes[j]["Name"],
					instance.axes[j]
				)
				for j in range(len(self.font.axes))
			]
			# print(sorted(order))
			key = [v[1] for v in sorted(order)]
			# Pad with zeroes so there are 5 values (Glyphs 2 axis limitation)
			while len(key) < 6:
				key.append(0)
			self.instance_keys[i] = "{%g, %g, %g, %g, %g, %g}" % tuple(key)
		# print(self.instance_keys)
	
	def export_stem_deltas(self, csv_path):
		"""
		Export the stem deltas to CVS at csv_path
		"""
		if "TTFStems" in self.hint_master.customParameters:
			stems = self.hint_master.customParameters["TTFStems"]
			csv = 'ppm;stem;'
			csv += ";".join(['%s' % instance.name for instance in self.font.instances])
			csv += "\n"
			for stem in stems:
				for ppm in range(8, 100):
					csv += '%3i;%s' % (ppm, stem.name())
					for i, instance in enumerate(self.font.instances):
						key = self.instance_keys[i]
						if stem.delta() is None:
							csv += ";  "
						elif key in stem.delta().keys():
							instance_delta = stem.delta()[key]
							if str(ppm) in instance_delta:
								csv += ';%+g' % instance_delta[str(ppm)]
							else:
								csv += ";  "
						else:
							csv += ";  "
					csv += "\n"
			with open(csv_path, "wb") as f:
				f.write(csv)
		else:
			print("Custom parameter 'TTFStems' is missing in hinted master.")
	
	def export_zone_deltas(self, csv_path):
		"""
		Export the zone deltas to CVS at csv_path
		"""
		pass
		
		

d = DeltaImportExport(Glyphs.font)
d.export_stem_deltas("bla.csv")
