import cv2
from Extension import method

class Processor (object):
    def __init__(self, color, inPath, outPath):
        self.color = color
        self.inPath=inPath
        self.outPath=outPath

    def processTask(self):
        print('Processing')
        method(self.color)
        
#processor = Processor('red', './images','./outImages')
#processor.processTask()

