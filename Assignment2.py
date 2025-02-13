
'''
Author: Nick Heyer
KUID: 3142337
Date: 2/13/25
Lab: Assignment2
Last modified: 2/13/25
EECS 348 Assignment 2
REGEX 
input: Assignment2_Test_File.txt
Output: all of the strings and patterns with match or no match with the match being shown
Collaborators: ChatGPT was used to find syntax errors, errors in my code for splitting the strings and patterns in the file and helping with error checking and making sure everything is valid with regex
'''
import re  #import regex

#opens and reads the file with the string and pattern
with open("Assignment2_Test_File.txt", "r") as file:
    lines = [line.strip() for line in file]#strips whitespace from lines

for line in lines:
    try:
        match = re.match(r"(.+?[.!?])\s(.+)", line)#error handling for the longer strings with spaces
        if match:
            string, pattern = match.groups()#gets the string and the pattern
        else:# splits at space if no punctuation is found bc of error checking
            parts = line.split(" ", 1)#error checking for using first space
            if len(parts) != 2: #error handling for 2 parts of the line
                print(f"Skipping invalid line: {line}") #prints
                continue #moves on
            string, pattern = parts

        regex = re.compile(pattern)# makes sure its valid

        match = regex.search(string)#searches for amtch of the pattern with the string given


        if match: # prints the results and whether it is a match or not with the match
            print(f"String: '{string}' / Pattern: '{pattern}' / Match: '{match.group()}'\n")
        else:
            print(f"String: '{string}' / Pattern: '{pattern}' / No match found \n")

    except re.error as e:
        print(f"Invalid regex pattern '{pattern}': {e}") #error message for invalid regex
