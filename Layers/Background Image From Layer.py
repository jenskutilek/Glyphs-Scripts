# MenuTitle: Background Image From Layer

from AppKit import (
    NSAffineTransform, NSBezierPath, NSBitmapImageFileTypeBMP, NSBitmapImageRep,
    NSColor, NSDeviceWhiteColorSpace, NSGraphicsContext, NSMakeRect, NSPoint)
from fontTools.misc.filenames import userNameToFileName
from GlyphsApp import Glyphs, GSBackgroundImage, Message
from pathlib import Path

__doc__ = """
Rasterize selected layers and set the raster image as background image. The image files
are saved next to the Glyphs file.
"""

PADDING = 100  # units
OVERSAMPLE = 2  # * upm


def image_from_layer(layer):
    bbox = layer.bounds
    x = bbox.origin.x - PADDING
    y = bbox.origin.y - PADDING
    width = (bbox.size.width + 2 * PADDING) * OVERSAMPLE
    height = (bbox.size.height + 2 * PADDING) * OVERSAMPLE
    img = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: E501
        None,  # bitmapDataPlanes
        width,  # pixelsWide
        height,  # pixelsHigh
        8,  # bitsPerSample
        2,  # samplesPerPixel
        True,  # hasAlpha
        False,  # isPlanar
        NSDeviceWhiteColorSpace,  # colorSpaceName
        0,  # bitmapFormat
        0,  # bytesPerRow
        0,  # bitsPerPixel
    )
    current = NSGraphicsContext.currentContext()
    context = NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
    NSGraphicsContext.setCurrentContext_(context)
    NSColor.whiteColor().set()
    NSBezierPath.fillRect_(NSMakeRect(0, 0, width, height))
    NSColor.blackColor().set()
    t = NSAffineTransform.alloc().init()
    t.translateXBy_yBy_(-x * OVERSAMPLE, -y * OVERSAMPLE)
    t.scaleBy_(OVERSAMPLE)
    t.transformBezierPath_(layer.bezierPath).fill()
    NSGraphicsContext.setCurrentContext_(current)
    return img


def save_background_image(layer, image):
    file_name = f"{layer.layerId}-{userNameToFileName(layer.parent.name)}.bmp"
    image_path = str(Path(layer.font().filepath).parent / file_name)
    data = image.representationUsingType_properties_(NSBitmapImageFileTypeBMP, None)
    data.writeToFile_atomically_(image_path, False)
    layer.backgroundImage = GSBackgroundImage(image_path)
    bbox = layer.bounds
    s = 1.0 / OVERSAMPLE
    layer.backgroundImage.position = NSPoint(
        bbox.origin.x - PADDING, bbox.origin.y - PADDING)
    layer.backgroundImage.scale = (s, s)


if Glyphs.font.filepath is None:
    Message("You must save the Glyphs file before a background image can be added.",
            title="Please save your file first")
else:
    for layer in Glyphs.font.selectedLayers:
        img = image_from_layer(layer)
        save_background_image(layer, img)
    print("OK")
