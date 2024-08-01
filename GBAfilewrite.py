
import operator
import os
from pprint import pprint

def add_word(word,dictionary):
    if word in dictionary:
        dictionary[word]  += 1
    else:
        dictionary[word] = 1
    return

def proccess_line(linein,gbaDict):
    badchars = [',', '.', '-', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in badchars:
        linein = linein.replace(char,' ') ## remove special chars as noted in badchars
    lineout = linein.split() ## parse line to create words ::: builds a list of words
    for newword  in lineout :
        add_word(newword,gbaDict)
    return

def pretty_print(dict):
    print("\n\nWord analysis of the Gettysburg Address")
    print("There are ",len(dict), " words in the Gettysburg Address")
    print('\n{0:<15}'.format("      WORD"), "Word Count\n")
    for k in sorted(dict, key=dict.get, reverse=True):
        print("     ",'{0:<12}'.format(k), dict[k])
    return

def putToFile(file,dict):
    text3 = '\n{0:<15}'.format("      WORD") + "Word Count\n"
    with open(file, 'a') as fileHandle:  # w for writing
        fileHandle.write(text3)
        for k in sorted(dict, key=dict.get, reverse=True):
            fileHandle.write("      " + '{0:<12}'.format(k) + str(dict[k])+"\n")
    return

### Main Method that creates the dictionary and opens the text file to be processed.
### as long as a line is present in the file this code calls the process_line function

def mymain():
    gbaDict = {}# empty dictionary created to capture words from the file
    gbaFile = open("gettysburg.txt", 'r')
    for line in gbaFile:
        if not line.isspace():### eliminates empty lines in the input file
            proccess_line(line,gbaDict)
    #####pretty_print(gbaDict)

    # textToWrite = 'testestestestest'
    # # text to be written is contained in the variable textToWrite
    # with open("GettyOut.txt", 'w') as fileHandle:  # w for writing
    #     fileHandle.write(textToWrite)  # write out text from a variable
    # fileHandle.close()
    fileToUse = input("Where would you like the dictionary analysis to go? ")
    if os.path.exists(fileToUse):
        os.remove(fileToUse)
        print("deleted File")
    print("Directory to Write to ", os.getcwd())
    text = "Word analysis of the Gettysburg Address\n\n"
    text2 = "There are " + str(len(gbaDict)) + " words in the Gettysburg Address\n"
    with open(fileToUse, 'a') as fileHandle:  # w for writing
        fileHandle.write(text)  # write out text from a variable
        fileHandle.write(text2)

    putToFile(fileToUse, gbaDict)
    fileHandle.close()
    pprint(gbaDict)
### Runs the code
mymain()
