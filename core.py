import os
import shutil
from Arguments import ArgumentResolver
from MyProc import Processor
    
def main():
    print("Hello World from main function!")
    
    resolver = ArgumentResolver()
    resolver.argumentSetup()

    color = input('Please input color you want to find ')
    
    processor = Processor(color, resolver.inputFolder(),resolver.outputFolder())
    processor.processTask()

if __name__ == "__main__":
    main()




    
