import sys


content = [x.strip().split() for x in open("data.dat").readlines()]

'''
Validations - 
    lines - 
        First line should be NUMBER then NAME OF THE GAME
        All lines following should be either D,L,or a number 
        Last line must contain 0 followed by END
    Rule validation-
        check for numbers and then check amount of light cells surrounding it and see if it matches number
        check for 2x2 blocks of dark cells
'''
