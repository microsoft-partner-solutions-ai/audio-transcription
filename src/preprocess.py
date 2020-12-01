"""
Usage: python preprocess.py <input_directory> <output_directory> 
Example: python preprocess.py data/raw data/preprocessed
Parameters: 
    <input_directory>: path to ground truth .txt files 
    <output_directory>: path to save the output preprocessed .txt files
Output: text that has been lowercased, stripped of punctuation other than apostrophes, stripped of 4 or more repeating characters and words in a row, and numbers spelled out
"""

import re, sys, os, glob
from num2words import num2words

def remove_punctuation(text):
        # punctuation characters to remove
        punc = '''!()[]{};:"\,<>./?@#$%^&*_~'''

        for char in text:
                if char in punc:
                        text = text.replace(char, '')
                if char == '-':
                        text = text.replace(char, ' ')
        return text

def is_ordinal(token):
        ordinal = False
        if token.endswith("th"):
                prefix = token.split("th")[0]
                if prefix.isnumeric():
                        ordinal = True
        return ordinal

def spell_numbers(text):
        tokens = text.split()
        for token in tokens: 
                if token.isnumeric():
                        number = remove_punctuation(num2words(token))
                        text = text.replace(token, number)
                elif is_ordinal(token):
                        prefix = token.split("th")[0]
                        number = remove_punctuation(num2words(prefix, to='ordinal')) 
                        text = text.replace(token, number)
        return text

def preprocess_text_file(in_file_path, out_file_path):
        in_file = open(in_file_path, 'r')
        out_file = open(out_file_path, 'w')

        text = in_file.readlines()

        # regex to remove all content before the utterance for each line 
        regex_rem_speaker_time = r'(^[^:\r\n]+:[ \t]*)+(.*[0-9]:[0-9][0-9])+([ \t]*)'
        subst_speaker_time = ""

        # regex to remove repeating characters more than four times 
        regex_repeat_char = r'(.)\1{3,}'
        subst_repeat_char = "\\1\\1\\1"

        # regex to remove repeating words more than four times
        regex_repeat_words = r'(\b(\w+)\b)(\s\1+){3,}'
        subst_repeat_words = "\\1 \\1 \\1"

        # regex to remove [] comments with timestamp
        regex_brk_time = r'(\[\w+)(?:\s\d{2}:\d{2}:\d{2})(\])'
        subst_brk_time = ""

        # regex to remove [] comments without time
        regex_brk = r'(\[\w+\])'
        subst_brk = ""

        # regex to remove () comments
        regex_paren = r'(\(\w+\))'
        subst_paren = ""
        
        # list to store the utterances 
        txt = []
        
        for line in text:
                # remove speakers and timestamps
                line = re.sub(regex_rem_speaker_time, subst_speaker_time, line)
                
                # lowercase
                line = line.lower()

                # replace new line with empty space
                line = ' '.join(line.split())
             
                # removing the [] comments with timestamp and without
                line = re.sub(regex_brk_time, subst_brk_time, line, re.MULTILINE)
                line = re.sub(regex_brk, subst_brk, line)

                # removing the () comments 
                line = re.sub(regex_paren, subst_paren, line)

                # remove punctuation
                line = remove_punctuation(line)

                # spell out the numbers 
                line = spell_numbers(line)

                # append non-empty lines to list of all lines
                if line:
                        txt.append(line)

        # join list of text into single string
        txt = ' '.join(txt)

        # avoid repeating words more than 4 times 
        txt = re.sub(regex_repeat_words, subst_repeat_words, txt, re.MULTILINE)

        # avoid repeating characters more than 4 times 
        txt = re.sub(regex_repeat_char, subst_repeat_char, txt, re.MULTILINE)

        # save output
        out_file.write(txt)

        # close files
        in_file.close()
        out_file.close()

def main(args):
        # parse arguments
        in_dir = args[0]
        out_dir = args[1]

        # create output directory if it doesn't exist
        if not os.path.exists(out_dir):
                os.makedirs(out_dir)
        
        # get all text filenames
        filenames = glob.glob(os.path.join(in_dir, '*.txt'))

        # preprocess each file 
        for filename in filenames:
                preprocess_text_file(filename, os.path.join(out_dir,filename.split('/')[-1]))

if __name__ == "__main__":
        main(sys.argv[1:])
