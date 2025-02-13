import re #import regex

with open("Assignment2_Test_File.txt", "r") as file: #opens specfic file to read over
    lines = [line.strip() for line in file] # strips the file
