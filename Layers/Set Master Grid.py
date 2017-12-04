#MenuTitle: Set Master Grid
# -*- coding: utf-8 -*-
__doc__="""
Set or delete the local grid for the current layer.
"""

import vanilla

plugin_key = "de.kutilek.MasterGrid"




def getGrid(master):
	grid = master.userData["%s.value" % plugin_key]
	if grid is not None:
		gx, gy = grid
	else:
		gx = gy = 0

	grid_type = master.userData["%s.type" % plugin_key]
	if grid_type is None:
		grid_type = "units"

	return gx, gy, grid_type


def setGrid(master, x, y=None, grid_type=None):
	if x is None:
		x = 0
	if x == 0:
		deleteGrid(master)
		return
	if y is None:
		y = x
	master.userData["%s.value" % plugin_key] = [x, y]
	if grid_type is None:
		if master.userData["%s.type" % plugin_key] is not None:
			del master.userData["%s.type" % plugin_key]
	else:
		master.userData["%s.type" % plugin_key] = grid_type


def deleteGrid(master):
	for key in ("value", "type"):
		full_key = "%s.%s" % (plugin_key, key)
		if master.userData[full_key] is not None:
			del master.userData[full_key]


def CurrentMaster():
	layer = Font.selectedLayers[0]
	master = layer.parent.parent.masters[layer.layerId]
	return master




class GridDialog(object):

	def __init__(self):
		self.w = vanilla.Window(
			(300, 160),
			"Master Grid", 
		)
		y = 8
		self.w.master_name = vanilla.TextBox((8, y, -8, 17), "Set local grid for master: None")
		
		y += 28
		x = 8
		self.w.label_x = vanilla.TextBox((x, y, 30, 17), "X:")
		self.w.x = vanilla.EditText((x + 22, y-3, 40, 24))
		x = 88
		self.w.label_y = vanilla.TextBox((x, y, 30, 17), "Y:")
		self.w.y = vanilla.EditText((x + 22, y-3, 40, 24))
		
		y += 32
		self.w.grid_type_label = vanilla.TextBox((8, y, 66, 17), "Grid is in:")
		self.w.grid_type = vanilla.RadioGroup(
			(74, y, -8, 40),
			["Absolute font units", "UPM subdivision"],
			isVertical = True,
		)
		
		self.w.button_cancel = vanilla.Button(
			(-272, -30, -204, -10),
			"Cancel",
			callback=self.callback_cancel,
		)
		self.w.button_delete = vanilla.Button(
			(-196, -30, -92, -10),
			"Remove Grid",
			callback=self.callback_delete,
		)
		self.w.button_set = vanilla.Button(
			(-84, -30, -8, -10),
			"Set Grid",
			callback=self.callback_set,
		)
		self.update()
		self.w.open()
		self.w.makeKey()
	
	
	def update(self):
		self.master = CurrentMaster()
		if self.master is None:
			self.w.master_name.set("Set local grid for master: None")
			self.w.x.set("0")
			self.w.y.set("0")
			
			self.w.x.enable(False)
			self.w.y.enable(False)
			self.w.grid_type.enable(False)
			self.w.button_delete.enable(False)
			self.w.button_set.enable(False)
		else:
			self.w.master_name.set("Set local grid for master: %s" % self.master.name)
			gx, gy, grid_type = getGrid(self.master)
			self.w.x.set(gx)
			self.w.y.set(gy)
			if grid_type == "div":
				self.w.grid_type.set(1)
			else:
				self.w.grid_type.set(0)
			
			self.w.x.enable(True)
			self.w.y.enable(True)
			self.w.grid_type.enable(True)
			self.w.button_delete.enable(True)
			self.w.button_set.enable(True)
		
	
	def callback_cancel(self, info):
		self.w.close()
	
	
	def callback_delete(self, info):
		deleteGrid(self.master)
		self.w.close()
	
	
	def callback_set(self, info):
		gx = self.w.x.get()
		gy = self.w.y.get()
		grid_type = self.w.grid_type.get()
		if grid_type == 0:
			grid_type = "units"
		else:
			grid_type = "div"
		try:
			gxi = int(gx)
			gyi = int(gy)
			gxf = float(gx)
			gyf = float(gy)
		except ValueError:
			print "Please enter a floating point number or an integer number."
			return
		if gxf == gxi:
			gx = gxi
		else:
			gx = gxf
		if gyf == gyi:
			gy = gyi
		else:
			gy = gyf
		setGrid(self.master, gx, gy, grid_type)
		self.w.close()




GridDialog()
