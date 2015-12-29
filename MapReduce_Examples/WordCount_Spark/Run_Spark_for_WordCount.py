
#----------------------------------------------
# This code is written in ipython pySpark shell 
#-----------------------------------------------


 # You can either read text into your Spark from local fileSystem:
     mySample_text_RDD = sc.textFile("file///directory_to_your_sample_text")
 # Or you can read from HDFS(dont forget to put your sample text into hdfs!)
     mySample_text_RDD = sc.textFile("/directory_of_your_sample_text_in_HDFS/")
 
 # You can see your first n line by the following command
     mySample_text_RDD.take(n)
 
 # Now mapper is as below:
     def split_words(line):
         return line.split()
      
     def create_pair(word):
         return (word, 1)
         
     pairs_RDD = mySample_text_RDD.flatMap(split_words).map(create_pair)
     
 # You can see your output by the following .collect() command
 
     pairs_RDD.collect()
     
 # Now Reducer is as short as follow:
 
     def sum_counts(a,b):
         return a+b
         
  # Now run reducer
  
      wordCounts_RDD = pairs_RDD.reduceByKey(sum_counts) 
      
 # Now lets se what we get as a result
 
     wordCounts_RDD.collect()
     
 
