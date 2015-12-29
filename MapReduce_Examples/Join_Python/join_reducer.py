

import sys


prev_key          = ""                #initialize previous word to be blank string
prev_value        = ""
total_views       = 0  #count input lines

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    #note: for simple debugging use print statements, ie:  
    curr_key  = key_value[0]         #key is first item in list, indexed by 0
    curr_val   = key_value[1]        #value is the second string, indexed by 1

#After mapper, your data's second entries will be either number or a channel name "ABC".
#After shuffling, they  will be sorted so that chanel name "ABC" will be at the bottom.
#You can debug reducer by this command:  cat join1_File*.txt | ./join_mapper.py | sort | ./join_reducer.py
# In the below code you should consider the diefferent edge cases and control them by if statments
    if prev_key != curr_key:
        total_views = 0; # eliminates the shows which are not in ABC, and resets the total_views
    
    if curr_val.isdigit() == True:
        local_views = int(curr_val)
        total_views = total_views + local_views
    

    if curr_val == 'ABC':
        print("{0}\t{1}".format(curr_key,total_views))
        total_views = 0 # reset the total_views as we are the end of the shows. 
                        #Next line will start with a new show and the value will be a number.(unless it is not the end of the list)
    
    prev_key = curr_key
   
  

	
