# MenuTitle: Insert Nodes At 45 Degrees

from AppKit import NSAffineTransform

def insert_node_at_45_degrees_path(path):
	m = NSAffineTransform().init()
	m.rotateByDegrees_(45)
	t = m.transformStruct()
	path.applyTransform((t.m11, t.m12, t.m21, t.m22, t.tX, t.tY))
	path.addNodesAtExtremes(checkSelection=True)
	m = NSAffineTransform().init()
	m.rotateByDegrees_(-45)
	t = m.transformStruct()
	path.applyTransform((t.m11, t.m12, t.m21, t.m22, t.tX, t.tY))

def insert_node_at_45_degrees(layer):
	for path in layer.paths:
		insert_node_at_45_degrees_path(path)

insert_node_at_45_degrees(Layer)