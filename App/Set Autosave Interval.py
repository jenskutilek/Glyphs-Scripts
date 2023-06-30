# Menutitle: Set Autosave Interval To 300 Seconds
from AppKit import NSDocumentController

NSDocumentController.sharedDocumentController().setAutosavingDelay_(300)
