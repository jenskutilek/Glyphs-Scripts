#MenuTitle: Apply UFO PS Hints
import xml.etree.ElementTree as ET

hintkey = "com.adobe.type.autohint"

		
def findNodeWithCoordinate(layer, pos, dist_direction=0, compare_pos=0, tolerance=1):
	# dist_direction 0 = vstem, we are looking for an x coordinate
	# dist_direction 1 = hstem, we are looking for a y coordinate
	# compare_pos is the secondary coordinate that will be compared to the current node's secondary coordinate
	# in order to find the closest matching node
	candidates = []
	for p in layer.paths:
		for n in p.nodes:
			diff = abs(pos - n.position[dist_direction])
			secondary_diff = abs(n.position[not dist_direction] - compare_pos)
			if diff <= tolerance:
				candidates.append((diff, secondary_diff, n))
	if candidates:
		candidates.sort(key=lambda d: (d[1], d[0]))
		#print "Candidates for", pos, compare_pos
		#for c in candidates:
		#	print "   ", c
		diff, _, n = candidates[0]
		return n
	else:
		return None
	

def getHint(layer, dist_direction, pos, width):
	originNode = findNodeWithCoordinate(layer, pos, dist_direction)
	if originNode is None:
		return None
	
	if width in (-20, -21):
		# This is a ghost hint
		newHint = GSHint()
		newHint.originNode = originNode
		#newHint.targetNode = targetNode
		newHint.horizontal = dist_direction
	else:
		origin_coords = originNode.position
		targetNode = findNodeWithCoordinate(layer, pos + width, dist_direction, origin_coords[not dist_direction])
		if targetNode is None:
			return None
	
		newHint = GSHint()
		newHint.originNode = originNode
		newHint.targetNode = targetNode
		newHint.horizontal = dist_direction
	
	return newHint


def applyHintsToLayer(layer):
	
	# Clear the current Glyphs hints
	layer.hints = []
	
	# Read XML data from the Adobe hinting from the UFO lib
	xml = layer.parent.userData[hintkey]
	if xml is None:
		return None
		
	# Parse the XML
	root = ET.fromstring(xml)
	hintsets = root.findall("hintset")
	for hintset in hintsets:
		for stem in hintset:
			if stem.tag == "vstem":
				dist_direction = 0
			elif stem.tag == "hstem":
				dist_direction = 1
			else:
				print "Unknown element '%s' in hintset of glyphs /%s." % (stem.tag, layer.parent.name)
				continue
			pos   = int(stem.attrib["pos"])
			width = int(stem.attrib["width"])
			hint = getHint(layer, dist_direction, pos, width)
			if hint is not None:
				layer.hints.append(hint)	
			else:
				print "Failed to apply %s at position %i, width %i." % (stem.tag, pos, width)


for layer in Glyphs.font.selectedLayers:
	applyHintsToLayer(layer)
	break