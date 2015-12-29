
import sys


for line in sys.stdin:
 
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0].split(" ")   #key is the first string in the line
    value_in   = key_value[1]   #value is the 2nd string in the line
 

    if  value_in == 'ABC' or value_in.isdigit() == True:
        print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string 

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value

