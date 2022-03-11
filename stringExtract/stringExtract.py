# Name: Alan Manuel
# File: plotTransferFunction.py
# Purpose: A script to plot a transfer function's bode magnitude and phase plots. Uses the scipy and matplot libraries.

import argparse
import sys
import fnmatch
import os


def stringExtract(text):
    

    #names of the benchmarks and predictors
    benchmarks = ['a2time01', 'bitmnp01', 'cacheb01', 'mcf', 'libquantum']
    predictors = ['BiModeBP', 'LocalBP', 'MultiperspectivePerceptron8KB', 'MultiperspectivePerceptron64KB', 'TournamentBP']

    #get the current working directory to open files.
    cd = os.getcwd()

    #set up a loop to read every benchmark and predictor.
    for benchmark in benchmarks:
        for predictor in predictors:
            filename = cd + f"\homework2\Homework2_{predictor}_{benchmark}_StatsFile.txt"
            print(f"Filename that will be opened: {filename}")
            #open every file for every predictor.
            f = open(filename, "r")


            #Set up an array to write all the data that we need if it is found.
            data = []
            #flag if data is found.
            flag = False

            #read all of the lines in a file.
            lines = f.readlines()

            for line in lines:
                
                #% of banch misprediction rate
                if "system.cpu.iew.branch_mispredict_rate" in line:
                    flag = True
                    data += [line]

                #execution time
                if "sim_seconds" in line:
                    flag = True
                    data += [line]

                #instrucitons per clock
                if "cpu.ipc" in line:
                    flag = True
                    data += [line]

                #% of branches
                if "system.cpu.iew.branch_percentage" in line:
                    flag = True
                    data += [line]

            #close file
            f.close()


            #if data is found, append the data to the text file.
            if flag == True:

                #open the output to append
                with open('outputHomework2Data.txt', 'a') as text_file:
                    text_file.write(f"Predictor: {predictor}  Benchmark: {benchmark}\n")
                    
                    #write the list elements in the file.
                    for datum in data:
                        text_file.write(datum)
                    
                    #spacing for next entry.
                    text_file.write("\n\n\n\n")

            




    return



##Parses the arguments in script call.
def getArgs():
    
    parser = argparse.ArgumentParser(description='extract and print string from all files in dierectory.')
    
    #create a group to hold required arguments.
    required = parser.add_argument_group("Required Aruments")

    #add each required arguemtns to the 'required' group.
    required.add_argument('-t', '--text', required=True, help = 'string to extract from file.')
    #required.add_argument('-f', '--fileName', required=True, help = 'path to the filename.')
    

    #prints help if no arguments are sent in.
    if len(sys.argv)== 1:
        parser.print_help()
        sys.exit(1)

    #return the parsed arguments.
    return parser.parse_args()
    


def main():

    args = getArgs()
    
    text = args.text


    
    stringExtract(text)


    
if __name__ == '__main__':
    main()