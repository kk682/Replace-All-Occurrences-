import os
import sys
import fileinput
import re

originalText = input("originalName")
replaceText = input("newName")
with open ("TextFile.txt", "r") as data:
    filedata = data.read()

# originalText="John is a smart student. john does not study for his exams."
newText = filedata.replace(originalText, replaceText)

newText = filedata.replace(originalText.lower(), replaceText)
with open ("TextFile.txt", "w") as data:
    filedata = data.write(newText)

