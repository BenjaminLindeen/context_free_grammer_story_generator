# CSCI 1913 Project 1 Spring 2022
# # Author: Benjamin Lindeen.

import time 
import csv
import cfg
from cfg import *

n_k = 0

def set_seed(new_seed):
    '''This function calls global variable n_k and assigns it to new_seed that is passed into the funciton, 
    while returning the new value of n_K'''
    
    global n_k
    n_k = new_seed
    return n_k

def next():
    '''This function assigns the rng variable to the formula for the park miller rng equation 
    with the global n_k variable acting as the seed'''
    
    rng = (((7 ** 5) * n_k) % ((2 ** 31) - 1))
    return(set_seed(rng))

def next_int(min, max):
    '''This function passes in minium and maximum values in order ot manipulate the rng next() function.
    using the min and max, a range function is defined as the difference between the two values
    the formula for getting a valuse between two numbers is applies as the random function, while returing the random value.'''

    range = max - min + 1
    random = ((next() % range) + min)
    return random

def random_choice(seq):
    '''This function takes in eihter a random sequence of lists of tuples, 
    and uses the next() rng function to to find a random element within the sequence'''
    
    random_seq = seq[next_int(min, max)]
    return random_seq
    
'''set seed to a pesudo random number based on computer clock'''

set_seed(int(time.time()))

def selection():
    ''' this funciton promts the user to enter the seleciton of furnctions for the rng'''
    
    try:
        selection = int(input("(1) Roll a dice. \n(2) Pick randomly. \n(3) Quit program.\nPick an option: "))
        print("You selected: " + str(selection))
        return int(selection)
    
    except:
        print("Please eneter a valid option, thank you! \n")
        return -1
    
def main():
    '''This function goes through all of the options for the user experience.
    it also goes through the logic to roll the dice and take in the random options'''
    
    do_while = True
    do = True
    options_list = []
    count = 0
    
    while do_while:
        select = selection()
        
        while select == -1:
            select = selection()
        
        if select == 1:
            try:
                dice_min = int(input("What is the minimum value of the die? "))
                dice_max = int(input("What is the maximum value of the die? "))
                dice_roll = int(input ("How many dice rolls? "))
                
                for roll in range(1, dice_roll + 1, 1):
                    dice = int(next_int(dice_min, dice_max))
                    count += dice
                    print("Roll: " + str(roll) + " Rolled: " + str(dice))

                print("The total of the dice rolled are " + str(count))
                do_while = False
                    
            except:
                print("die inputs must be an integer")
    
        elif select == 2:
            while do:
                options = input("Enter data or press enter: ")
                
                if options == "":
                    do = False
                else:
                    options_list.append(options)

            for pick in options_list:
                choose = int(next_int(0, len(options_list)))
                
            print("The random reault was: " + options_list[choose])
            do_while = False  
            
        elif select == 3:
            print("The program has quit, have a nice day!")
            do_while = False
        
if __name__ == "__main__":
    '''conditional run of main'''
    
    main()