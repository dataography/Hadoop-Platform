#
#   COURSERA ASSIGNEMNTS AND EXAMPLES  #

import sys             #a python module with system functions for this OS

# ------------------------------------------------------------
##################### MAPPER FUNCTION ########################
#This mapper code will input a line of text and output <word, 1>
# ------------------------------------------------------------
for line in sys.stdin:  
#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    line = line.strip()  #strip is a method, ie function, associated  with string variable, it will strip  the carriage return 
    keys = line.split()  #split line at blanks (by default), and return a list of keys(words)
    for key in keys:     #a for loop through the list of keys
        value = 1        
        print('{0}\t{1}'.format(key, value) ) #the {} is replaced by 0th,1st items in format list  #also, note that the Hadoop default is 'tab' separates key from the value

#This mapper code will input a line of text and output <word, 1>. After groupun and shuffling they will processed by Reducer.py


