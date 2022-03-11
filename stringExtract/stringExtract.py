# Name: Alan Manuel
# File: plotTransferFunction.py
# Purpose: A script to plot a transfer function's bode magnitude and phase plots. Uses the scipy and matplot libraries.

import argparse
import sys
import fnmatch



def stringExtract(fileName, text):


    return



##Parses the arguments in script call.
def getArgs():
    
    parser = argparse.ArgumentParser(description='extract and print string from all files in dierectory.')
    
    #create a group to hold required arguments.
    required = parser.add_argument_group("Required Aruments")

    #add each required arguemtns to the 'required' group.
    required.add_argument('-s', '--string', 't', '--text', required=True, help = 'string to extract from file.')
    required.add_argument('-f', '--fileName', required=True, help = 'path to the filename.')
    

    #prints help if no arguments are sent in.
    if len(sys.argv)== 1:
        parser.print_help()
        sys.exit(1)

    #return the parsed arguments.
    return parser.parse_args()
    


def main():
    #print("In main")
    args = getArgs()
    

    
    stringExtract(text, filename)


    
if __name__ == '__main__':
    main()