
#This join task is the one of the assignment in Coursera which is written pySpark shell on Cloudera Virtual Machine

# Loading the first data file

in[]: fileA = sc.textFile("file:///home/cloudera/join1_FileA.txt")

#see content and the format of the data
in[]: fileA.collect() # shows you data
out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']

#Loading the second data file
in[]: fileB = sc.textFile("file:///home/cloudera/join1_FileB.txt")

#see content and the format of the data
in[]: fileB.collect()
out[]:
[u'Jan-01 able,5',
 u'Feb-02 about,3',
 u'Mar-03 about,8',
 u'Apr-04 able,13',
 u'Feb-22 actor,3',
 u'Feb-23 burger,5',
 u'Mar-08 burger,2',
 u'Dec-15 able,100']

in[]: def split_fileA(line):
          temp = line.split(",")
          word = temp[0]
          count = int(temp[1])
          return (word,count) 

in[]: fileA_data = fileA.map(split_fileA)
in[]: fileA_data.collect()
#after spliting we get the following data
out[]: [(u'able', 991), (u'about', 11), (u'burger', 15), (u'actor', 22)]

in[]: def split_fileB(line):
          temp = line.split(" ")
          date = temp[0]
          temp1 = temp[1].split(",")
          word = temp1[0]
          count_string=temp1[1]
          return (word, date + " " + count_string)

in[]: fileB_data = fileB.map(split_fileB)
in[]: fileB_data.collect()
#after spliting the element of file B, we get
out[]: 
[(u'able', u'Jan-01 5'),
 (u'about', u'Feb-02 3'),
 (u'about', u'Mar-03 8'),
 (u'able', u'Apr-04 13'),
 (u'actor', u'Feb-22 3'),
 (u'burger', u'Feb-23 5'),
 (u'burger', u'Mar-08 2'),
 (u'able', u'Dec-15 100')]

in[]: fileB_joined_fileA = fileB_data.join(fileA_data)
in[]: fileB_joined_fileA.collect()
#after joining two set we get final output
out[]: 
[(u'about', (u'Feb-02 3', 11)),
 (u'about', (u'Mar-03 8', 11)),
 (u'able', (u'Jan-01 5', 991)),
 (u'able', (u'Apr-04 13', 991)),
 (u'able', (u'Dec-15 100', 991)),
 (u'actor', (u'Feb-22 3', 22)),
 (u'burger', (u'Feb-23 5', 15)),
 (u'burger', (u'Mar-08 2', 15))]
