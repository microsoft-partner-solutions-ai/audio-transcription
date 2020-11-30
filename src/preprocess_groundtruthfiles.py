import csv
import sys
import pandas as pd
import re

# open and read lines from file
txtfile = r"C:\Users\dthakar\Desktop\GroundTruthTXTFiles\Ground truth_Assault of Domino’s Delivery Driver - Seattle PD.txt"
file = open(txtfile,'r')
text = file.readlines()

# regex to remove all content before the utterance for each line 
regex_rem_speaker_time = r'(^[^:\r\n]+:[ \t]*)+(.*[0-9]:[0-9][0-9])+([ \t]*)'
subst_speaker_time = ""

# regex to remove repeating characters more than four times 
regex_repeat_char = r'(.)\1+'
subst_repear_char = "\\1\\1"

# punctuation characters to remove
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

# list to store the utterances 
txt = []

for test_str in text:
        # print(re.sub(regex, subst, test_str))

        # lowercase
        test_str = test_str.lower()
        # replace new line with empty space
        test_str = test_str.replace('\n','')
        # get rid of punctuation

        # avoid repeating characters more than 4 times

        # avoid repeating words more than 4 times 

        #removing the [inaudible] comments

        #spell out the numbers - inflect package 

        # substitute regex match with empty space for all lines in text file
        txt.append(re.sub(regex_rem_speaker_time, subst_speaker_time, test_str))
print(txt)


