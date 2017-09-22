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
			if n.type == OFFCURVE:
				continue
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
	

def getHint(layer, dist_direction, pos, width, guess_ghost_direction=True, point_snap_tolerance=0):
	originNode = findNodeWithCoordinate(
		layer,
		pos,
		dist_direction,
		compare_pos = 0,
		tolerance = point_snap_tolerance
	)
	if originNode is None:
		return None
	
	if width in (-20, -21):
		# This is a ghost hint
		newHint = GSHint()
		if width == -20:
			newHint.type = TOPGHOST
		else:
			newHint.type = BOTTOMGHOST
			
			if guess_ghost_direction:
				# vfb2ufo stores all ghost links as -21 ...
				# we have to guess if it should rather be a top ghost hint
				for z in layer.parent.parent.masters[layer.associatedMasterId].alignmentZones:
					if z.size > 0:
						if z.position <= pos <= z.position + z.size:
							newHint.type = TOPGHOST
							break
		
		newHint.originNode = originNode
		newHint.horizontal = dist_direction
	else:
		origin_coords = originNode.position
		targetNode = findNodeWithCoordinate(
			layer,
			pos + width,
			dist_direction,
			compare_pos = origin_coords[not dist_direction],
			tolerance = point_snap_tolerance
		)
		if targetNode is None:
			return None
	
		newHint = GSHint()
		newHint.originNode = originNode
		newHint.targetNode = targetNode
		newHint.horizontal = dist_direction
	
	return newHint


def applyHintsToLayer(layer, guess_ghost_direction=True, point_snap_tolerance=0):
	
	# Clear the current Glyphs hints
	layer.hints = []
	
	# Read XML data from the Adobe hinting from the UFO lib
	xml = layer.parent.userData[hintkey]
	if xml is None:
		return None
		
	# Parse the XML
	root = ET.fromstring(xml)
	hintsets = root.findall("hintset")
	seen_hints = []
	for hintset in hintsets:
		for stem in hintset:
			if stem.tag == "vstem":
				hint_list = [(0, stem.attrib["pos"], stem.attrib["width"])]
			
			elif stem.tag == "hstem":
				hint_list = [(1, stem.attrib["pos"], stem.attrib["width"])]
			
			elif stem.tag == "vstem3":
				values = stem.attrib["stem3List"].split(",")
				hint_list = [(0, values[i], values[i+1]) for i in range(0, len(values), 2)]
			
			elif stem.tag == "hstem3":
				values = stem.attrib["stem3List"].split(",")
				hint_list = [(1, values[i], values[i+1]) for i in range(0, len(values), 2)]
			
			else:
				print "Unknown element '%s' in hintset of glyphs /%s." % (stem.tag, layer.parent.name)
				print xml
				continue
			
			for dist_direction, pos, width in hint_list:
				hint = getHint(layer, dist_direction, float(pos), float(width), guess_ghost_direction, point_snap_tolerance)
				if hint is not None:
					if (dist_direction, pos, width) not in seen_hints:
						layer.hints.append(hint)
						seen_hints.append((dist_direction, pos, width))
					# else skip hint from a different hint set with the same direction, position and width
				else:
					print "Failed to apply %s at position %i, width %i in glyph %s." % (stem.tag, float(pos), float(width), layer.parent.name)


for layer in Glyphs.font.selectedLayers:
	applyHintsToLayer(layer, guess_ghost_direction=True, point_snap_tolerance=0)
