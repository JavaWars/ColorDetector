import argparse

class ArgumentResolver(object):
    
    def __init__(myResolver):
        print('Constructor')
        myResolver.parser = argparse.ArgumentParser()
        myResolver.storedParam = ''

    def argumentSetup(obj):

        obj.parser.add_argument('--inFolder', type=str, default='./images', help='Input directory')
        obj.parser.add_argument('--outFolder', type=str, default='./output', help='Output directory')
        obj.parser.add_argument('--supportedColor', type=str, default='./red green blue yellow', help='Supported color')

        obj.storedParam = obj.parser.parse_args()

        return obj.storedParam

    def inputFolder(self):
        return self.storedParam.inFolder

    def outputFolder(self):
        return self.storedParam.outFolder

    def supportedColor(self):
        return self.storedParam.supportedColor

