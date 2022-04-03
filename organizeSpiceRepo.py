# Name: Alan Manuel
# File: organizeSpiceRepo.py
# Purpose: Change spice model repository file struture from [symbol, library, schematic] to [Part1, Part2, , ..., PartN] 

import argparse
from distutils.log import error
from errno import EEXIST
from msilib.schema import File
import os
import glob
import time
import shutil



#DEBUG Parameter.
DEBUG = False





#these are the wildcards that need to be applied to extract part names.
SPICE_MODEL_FOLDERS = ['symbols', 'libraries', 'schematics']
SPICE_MODEL_FILE_TYPES = ['asy', 'lib', 'asc']


#main function
def organizeSpiceRepo():


    #finds the files inside the directory that are within two folders and places them in a list
    allFiles = gatherAllParts()
    
    
    #making a list that contains all unique parts with file extentions and without file extentions.
    uniqueParts = gatherUniquePartFiles(allFiles, removeFileExtentsion=True)

    print(uniqueParts)



    

    #generate empty folders to place uniqe parts in.
    generateApexPartFolderNames(uniqueParts)

    #populates the folders with unique parts.
    populateFolders(allFiles, uniqueParts)




    return


#populates the part folders with the circuit, library, and schematics for the parts.
def populateFolders(allFiles, uniqueParts):

    directory = 'GeneratedSpiceModelList'
    parentPath = os.path.join(os.getcwd(), directory)

    for part in uniqueParts:

        print('in Part:')
        print(part)


        for file in allFiles:
            print('in file:')
            print(file)

            #change list element into a string
          
            file = formatFileName(file)





            if part in file:
                #set file extension to lowercase
                print(f'Part: {part} found in file: {file}')

                copyPath = (parentPath + '\\' + part + '\\' + part + '.' + file[-3:].lower())




                try:
                    print(f'Copying File into: {copyPath}')
                    shutil.copyfile(file, copyPath)
                except error:
                    print(error)






    return


#makes the file extention lowercase.
def formatFileName(name):

    name = ''.join(name)

    lowercaseExtension = name[-3:].lower()
    name = name[:-3] + lowercaseExtension
    
    return name


#generates a folder for each part.
def generateApexPartFolderNames(uniqueParts):

    #generating a parent folder to house all of the parts.
    directory = 'GeneratedSpiceModelList'
    path = os.path.join(os.getcwd(), directory)



    #generate a directory, if it exists, notify the user and do nothing
    try:
        os.mkdir(path)
    except FileExistsError:
        debug('The \'GeneratedSpiceModelList\' folder already exists. Operation will coninue as normal', 0.01)




    

    #print
    
    folders = []
    for part in uniqueParts:
        
        newFolderPath = path + '\\' + part

        folders.append(newFolderPath)
    
    
    if(DEBUG):
        debug('Folders to be generated')
        debug(folders)
    

    for folder in folders:
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
            #debug(f'Warning: File Folder: \'{folder}\' exists and was not re-made.', 0.01)

    return






#generates a list of all the files that contain apex parts in the directory.
def gatherAllParts():


    #generate a list of all files that are parts.
    apexParts = glob.glob(os.getcwd() + r'\repodump\*\*')

    #sort the parts.
    apexParts.sort


    if(DEBUG):
        debug('All parts list generated:')
        debug(apexParts)

    #return the generated list.
    return apexParts




#this function takes all the parts in the list that is passed in and then generates a list of unique apex parts.
def gatherUniquePartFiles(apexParts, removeFileExtentsion=False):

    #generate a list of all the parts that are present in the list that is sent in.
    uniqueParts = []
    for part in apexParts:

         
        #these are the wildcards that need to be applied to extract part names.
        filefolders = SPICE_MODEL_FOLDERS
        fileTypes = SPICE_MODEL_FILE_TYPES
        
        #format the filename so that it can be trimmed
        part = part.lower()

        #trim the part name
        for folder in filefolders:
            for fileType in fileTypes:

                #removeprefix removes all the text from the left side that matches the argument
                #removesuffix removes all the text from the right side that matches the argument.
                
                part = part.removeprefix(os.getcwd().lower() + f'\\repodump\\{folder}\\'.lower())
                
                if(removeFileExtentsion == True):
                    part = part.removesuffix(f'.{fileType}'.lower())


                

        #set part names to uppercase
        part = part.upper()

        #apped the part to the list of unique parts.
        uniqueParts.append(part)


    #remove duplicate part names
    uniqueParts = list(set(uniqueParts))

    if(DEBUG):
        debug('\nGenerated List of unique parts:')
        debug(uniqueParts)
        

    #return the generated list.
    return uniqueParts

#prints a debug message with time for the reader to read
def debug(message, printWaitTime=1):


    #allows lists to be printed.
    if type(message) == list:
        printWaitTime = 0.01

        for element in message:
                print(element)
                time.sleep(printWaitTime)

    else:
        print(message)
        time.sleep(printWaitTime)

    return

##Parses the arguments in script call.
def getArgs():
    
    parser = argparse.ArgumentParser(description='Runs a script on to make spice repository file structure house every part\'s components.')

    return parser.parse_args()
    

#this is obviously the main function...
def main():
    #print("In main")
    args = getArgs()

    organizeSpiceRepo()


    
if __name__ == '__main__':
    main()
