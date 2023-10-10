# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math # for binary search function
import time # for calculating time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    #main menu options
    print("\nMain Menu")
    print("1: Spell Check a Word(Linear Search)")
    print("2: Spell Check a Word(Binary Search)")
    print("3: Spell Check Alice in Wonderland (Linear Search)")
    print("4: Spell Check Alice in Wonderland (Binary Search)")
    print("5: Exit")
    #input from user 
    selection = input("Enter menu selection (1-5): ")

    #action based on input
    if selection == "1":
        spellCheckLinear(dictionary)
    elif selection == "2":
        spellCheckBinary(dictionary)
    elif selection == "3":
        aliceWonderLinear(aliceWords, dictionary)
    elif selection == "4":
        aliceWonderBinary(aliceWords, dictionary)
    elif selection == "5":
        print("Bye for now :-)")


# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(anArray, item):
    for x in range(len(anArray)):
        if anArray[x] == item:
            return x
    # if item not found
    return -1

def binarySearch(anArray, item):
    li = 0
    ui = len(anArray) - 1
    while li <= ui:
        mi = math.floor((li + ui) / 2)
        if item == anArray[mi]:
            return mi
        elif item < anArray[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    #if item not found
    return -1

def spellCheckLinear(array):
    wordEnter = input("Please enter a word: ").lower()
    print("\nLinear Search starting...")
    #search for item
    startTime = time.time()
    searchItem = linearSearch(array, wordEnter)
    endTime = time.time()
    if searchItem >= 0:
        print(f"{wordEnter} is in the dictionary at position {searchItem}. (", startTime - endTime, " seconds)")
    else:
        print(f"{wordEnter} is NOT IN the dictionary. (", endTime - startTime, " seconds)")

def spellCheckBinary(array):
    wordEnter = input("Please enter a word: ").lower()
    print("\nBinary Search starting...")
    #search for item
    startTime = time.time()
    searchItem = binarySearch(array, wordEnter)
    endTime = time.time()
    if searchItem >= 0:
        print(f"{wordEnter} is in the dictionary at position {searchItem}. (", startTime - endTime, " seconds) ")
    else:
        print(f"{wordEnter} is NOT IN the dictionary. (", endTime - startTime, " seconds)")

def aliceWonderLinear(aliceWords, dictionary):
    #counter
    notWords = 0
    #search alice list for words NOT (return -1) in dictionary
    startTime = time.time()
    for i in aliceWords:
        if linearSearch(dictionary, i) == -1:
            notWords += 1
    endTime = time.time()
    print(f"Number of words not found in dictionary: {notWords} (", endTime - startTime, " seconds)")        

def aliceWonderBinary(aliceWords, dictionary):
    #counter
    notWords = 0
    #search alice list
    startTime = time.time()
    for i in aliceWords:
        if binarySearch(dictionary, i) == -1:
            notWords += 1
    endTime = time.time()
    print(f"Number of words not found in dictionary: {notWords} (", endTime - startTime, " seconds)")

# Call main() to begin program
main()
