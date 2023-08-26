
# CSCI 1913 Project 1 Spring 2022
# Author: Benjamin Lindeen

import time
import csv 
from my_rng import *

# set_seed(int(time.time()))

def new_grammar():
    new_grammar = {}
    return new_grammar
    
def add_rule(grammar, left, right):
    left = ""
    right = []
    
    return left

def generate(grammar):
    grammar_string = ""
    
    for row in grammar:
        grammar_string += str(grammar.get(row))
    
    for index in range(0, len(grammar_string), 1):
        random = grammar_string[next_int(0, len(grammar_string))]
    
    return random
    
def grammar_from_file(filename):
    '''This function passes in the name of a file and attempts to read the file.
    it reads the csv file, and iterates over the variables and replacements in the csv file.
    it stores the values from the variables as keys for a dictionary.
    from there it checks to see if the key in the dictionary are duplicates, 
    if so it dynamically allocates a list and assigns the further replacements to the elements of the list.'''
    
    grammar = new_grammar()
    
    try:
        reader = csv.DictReader(open(filename))
    
    except:
        print("The file that you are looking for does not exist.")
        return

    for row in reader:
        Variable = row["variable"]
        Replacement = row["replacement"]
        
        if Variable in grammar:
            grammar[Variable].append(Replacement)
        
        else:
            grammar[Variable] = [Replacement]
        
    return grammar

def main():
    ''' this function prompts the user to enter a file name, it then calls the grammar_from_file function with the file name passed in'''
    
    file_choose = input("What is the name of the file that should be read? ")    
    grammar_from_file(file_choose)
    
    print(generate(grammar_from_file(file_choose)))
       
if __name__ == "__main__":
    '''conditional run of main'''
    
    main()