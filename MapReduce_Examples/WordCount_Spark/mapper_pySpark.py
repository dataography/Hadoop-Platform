# Mapper for word count written in pySpark: 
def split_word(line):      # takes input as a string. ex in: "the good the bad and the ugly"
    return line.split()    # returns splited list of words. ex out: ['the', 'good', 'the', 'bad', 'and', 'the', 'ugly']
    
def create_pair(word):     # takes words(in string format) ex in: 'the'
    return (word, 1)       # returns a pair (word, 1). ex out: ('the', 1) 
