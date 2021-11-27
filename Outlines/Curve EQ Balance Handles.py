# MenuTitle: CurveEQ: Balance Handles

"""
Triangle Geometry helpers
"""

from math import atan2, cos, pi, sin, sqrt
from GlyphsApp import Glyphs, GSOFFCURVE


# helper functions


def getTriangleArea(a, b, c):
	return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)


def isOnLeft(a, b, c):
	if getTriangleArea(a, b, c) > 0:
		return True
	return False


def isOnRight(a, b, c):
	if getTriangleArea(a, b, c) < 0:
		return True
	return False


def isCollinear(a, b, c):
	if getTriangleArea(a, b, c) == 0:
		return True
	return False


def distance(p0, p1, doRound=False):
	# Calculate the distance between two points
	d = sqrt((p0.x - p1.x) ** 2 + (p0.y - p1.y) ** 2)
	if doRound:
		return int(round(d))
	else:
		return d


# Triangle Geometry

# p0 is the first point of the Bezier segment and p3 the last point.
# p1 is the handle of p0 and p2 the handle of p3.

# A triangle is formed:
# b = hypotenuse, the line from p0 to p3
# a = p0 to I with I being the intersection point of the lines p0 to p1 and p3 to p2
# c = p3 to I "

# alpha = the angle between p0p1 and p0p3
# beta  = the angle between p3p0 and p3p2
# gamma = the angle between p3I and p0I


def getTriangleAngles(p0, p1, p2, p3):

	# Calculate the angles

	alpha1 = atan2(p3.y - p0.y, p3.x - p0.x)
	if p1.y == p0.y and p1.x == p0.x:
		# Zero handle p0-p1, use p2 as reference
		alpha2 = atan2(p2.y - p0.y, p2.x - p0.x)
	else:
		alpha2 = atan2(p1.y - p0.y, p1.x - p0.x)
	alpha = alpha1 - alpha2

	gamma1 = atan2(p3.x - p0.x, p3.y - p0.y)
	if p3.x == p2.x and p3.y == p2.y:
		# Zero handle p3-p2, use p1 as reference
		gamma2 = atan2(p3.x - p1.x, p3.y - p1.y)
	else:
		gamma2 = atan2(p3.x - p2.x, p3.y - p2.y)
	gamma = gamma1 - gamma2

	beta = pi - alpha - gamma

	return alpha, beta, gamma


def getTriangleSides(p0, p1, p2, p3):
	alpha, beta, gamma = getTriangleAngles(p0, p1, p2, p3)

	# Calculate the sides of the triangle

	b = abs(distance(p0, p3))
	a = b * sin(alpha) / sin(beta)
	c = b * sin(gamma) / sin(beta)

	return a, b, c


def getNewCoordinates(
	targetPoint, referencePoint, alternateReferencePoint, distance
):
	if targetPoint.y == referencePoint.y and targetPoint.x == referencePoint.x:
		phi = atan2(
			alternateReferencePoint.y - referencePoint.y,
			alternateReferencePoint.x - referencePoint.x,
		)
	else:
		phi = atan2(
			targetPoint.y - referencePoint.y, targetPoint.x - referencePoint.x
		)
	x = referencePoint.x + cos(phi) * distance
	y = referencePoint.y + sin(phi) * distance
	return (x, y)


"""
EQMethods.Balance
"""

# Adjustment factor for curves with zero handles
tension_adjust = 1.18


def eqBalance(p0, p1, p2, p3):

	# Check for zero handles
	factor = 1
	zero = False
	if p1.y == p0.y and p1.x == p0.x:
		factor = tension_adjust
		zero = True
		if p3.y == p2.y and p3.x == p2.x:
			# Both zero handles
			return p1, p2  # or use thirds?
	else:
		if p3.y == p2.y and p3.x == p2.x:
			factor = tension_adjust
			zero = True

	alpha = atan2(p1.y - p0.y, p1.x - p0.x)
	beta = atan2(p2.y - p3.y, p2.x - p3.x)

	if abs(alpha - beta) >= 0.7853981633974483:  # 45°
		# check if both handles are on the same side of the curve
		if (
			zero
			or isOnLeft(p0, p3, p1)
			and isOnLeft(p0, p3, p2)
			or isOnRight(p0, p3, p1)
			and isOnRight(p0, p3, p2)
		):

			a, b, c = getTriangleSides(p0, p1, p2, p3)

			# Calculate current handle lengths as percentage of triangle side length
			ca = distance(p3, p2) / a
			cc = distance(p0, p1) / c

			# Make new handle length the average of both handle lenghts
			handle_percentage = (ca + cc) / 2 * factor

			# Scale triangle sides a and c by requested handle length
			a = a * handle_percentage
			c = c * handle_percentage

			# move first control point
			x1, y1 = getNewCoordinates(p1, p0, p2, c)

			# move second control point
			x2, y2 = getNewCoordinates(p2, p3, p1, a)

			p1.x = x1
			p1.y = y1

			p2.x = x2
			p2.y = y2

	return p1, p2

	
def balance_segment(segment):
	p0, p1, p2, p3 = segment
	eqBalance(p0, p1, p2, p3)

	
def balance_layer(layer):
	segments = []
	first_offcurve = True
	for path in layer.paths:
		node_index = 0
		for n in path.nodes:
			if n.type == GSOFFCURVE:
				if first_offcurve:
					# Skip first offcurve point
					first_offcurve = False
				else:
					if n in layer.selection:
						segments.append([
							path.nodeAtIndex_(node_index - 2),
							path.nodeAtIndex_(node_index - 1),
							n,
							path.nodeAtIndex_(node_index + 1)
						])
					first_offcurve = True
			node_index += 1
	
	[balance_segment(s) for s in segments]


if Glyphs.font is not None:
	layer = Glyphs.font.selectedLayers[0]
	balance_layer(layer)
