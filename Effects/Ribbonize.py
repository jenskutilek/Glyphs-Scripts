#for i in range(0x1D00, 0x1DC0):
#	print "uni%04X" % i

#FLM: jkRibbonize
# Farbbandeffekt
# (C) Jens Kutilek 2009

# Einstellungen

# Schrittweite der einzelnen Rasterpunkte in units
resx = 20
resy = 20

# Minimaler und maximaler Radius der Rasterpunkte in units
lmin = 6
lmax = 17

# Streuung der einzelnen Rasterpunkte
# Zwischen (-vx|-vy) und (vx|vy)
vx = 2
vy = 2

# Wieviele Ecken hat ein Rasterpunkt
corners = 7

# Minimaler und maximaler Anschlagdruck pro Buchstabe
pmin = 3 # 7
pmax = 10

gradientFactor = 2.2

# Suffix fuer neue Glyphnamen
suffix = ".002"

from robofab.world import CurrentFont, CurrentGlyph
from random import randint, random
from math import pi
from time import time
from jkRFTools.drawing import drawCircle, drawNAgon

def ribbonGlyph(source, dest, pressure):
	global resx, resy, lmin, lmax, vx, vy, corners, gradientFactor
	# find out how big the shape is from the glyph.box attribute
	xMin, yMin, xMax, yMax = source.box
	
	# get a pen to draw in the new glyph
	myPen = dest.getPen()
	
	lmin2 = int(round(lmin*pressure))
	lmax2 = int(round(lmax*pressure))
	
	#print "lmin2:", str(lmin2)
	#print "lmax2:", str(lmax2)
	
	# draw from top to bottom
	yValues = range(yMin, yMax, resy)
	yValues.reverse()
	
	yAmplitude = yMax - yMin
	print("Amplitude:", yAmplitude, "=", yMax, "-", yMin)
	# go for it!
	for y in yValues:
		gradientCorrection = gradientFactor - gradientFactor * (y - yMin) / yAmplitude
		#print "y:", y, " gradient corr =", gradientCorrection
		for x in range(xMin, xMax, resx):
			# check the source glyph is white or black at x,y
			if source.pointInside((x, y)):
				size = randint(lmin2, lmax2)*2
				#if size > 5: # no small circles
				#drawCircle(myPen, x+randint(-vx, vx), y+randint(-vy, vy), size)
				
				phi = (2 * pi * random()) / corners
				#print "Rotation:", phi/pi, "pi"
				
				myX = x+randint(-vx, vx)
				myY = y+randint(-vy, vy)
				
				#drawCircle(myPen, myX, myY, size)
				drawNAgon(pen=myPen, x=myX, y=myY, size=int(round((1 + gradientCorrection)*size)), n=corners, rt=phi)


# main

f=CurrentFont()

glyphnames = f.selection

start = int(round(time()))

for sourcename in glyphnames:
	source = f[sourcename]
#	if not(source.name[-6:-1] == ".calt"):
	if not(f.has_key(source.name+suffix)):
		dest = f.newGlyph(source.name+suffix)
	else:
		dest = f[source.name+suffix]
		dest.clear()
	dest.width = source.width
	pressure = float(randint(pmin,pmax))/10
	print "Ribbonize glyph "+source.name+" with pressure= "+str(pressure)
	ribbonGlyph(source, dest, pressure)
	dest.removeOverlap()

stop = int(round(time()))
if len(glyphnames) > 0:
	print("\nFinished. Time per glyph:", (stop-start)/len(glyphnames), "seconds")
