import os
import sys
import fileinput
import re

# originalText="John is a smart student. john does not study for his exams."
originalText = input("originalName")
# replaceText="brian is a smart student. john does not study for his exams."
replaceText = input("newName")
with open ("TextFile.txt", "r") as data:
    filedata = data.read()

newText = filedata.replace(originalText, replaceText, 1)
with open ("TextFile.txt", "w") as data:
    filedata = data.write(newText)
