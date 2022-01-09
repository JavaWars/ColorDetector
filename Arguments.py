import argparse

class ArgumentResolver(object):
    
    def __init__(myResolver):
        print('Constructor')
        myResolver.parser = argparse.ArgumentParser()
        myResolver.storedParam = ''

    def argumentSetup(obj):

        obj.parser.add_argument('--inFolder', type=str, default='./images', help='Input dirrectory')
        obj.parser.add_argument('--outFolder', type=str, default='output', help='Output directory')

        obj.storedParam = obj.parser.parse_args()

        return obj.storedParam

    def inputFolder(self):
        return self.storedParam.inFolder

    def outputFolder(self):
        return self.storedParam.outFolder
    

#resolver = ArgumentResolver()
#resolver.argumentSetup()
#print(resolver.inputFolder())
