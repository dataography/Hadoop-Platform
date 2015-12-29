

###################################################################
######  TASK: Find the total views for the channel ABC.
###################################################################
######  DATA TYPES AND CONTENTS:  

join_gennum*.txt contains following data: The list of <shows, views>

    Almost_News, 25
    Hourly_Show,30
    Hot_Cooking,7
    Almost_News, 35
    Postmodern_Family,8
    Baked_News,15
    Dumb_Games,60
    …

join_genchan*.txt contains following data: The list of <shows, channel> 

    Almost_News, ABC
    Hourly_Show, COM
    Hot_Cooking, FNT
    Postmodern_Family, NBC
    Baked_News, FNT
    Dumb_Games, ABC
    …
 If you are using Cloudera VM, you can download the file  by runnin the following commands in terminal:
 
    python make_join2data.py y 1000 13 > join2_gennumA.txt
    python make_join2data.py y 2000 17 > join2_gennumB.txt
    python make_join2data.py y 3000 19 > join2_gennumC.txt
    python make_join2data.py n 100  23 > join2_genchanA.txt
    python make_join2data.py n 200  19 > join2_genchanB.txt
    python make_join2data.py n 300  37 > join2_genchanC.txt
 
 

1- Type following commands in terminal and copy-past or directly download the join_mapper.py  and join_reducer.py 

    > gedit join_mapper.py

    > gedit join_reducer.py

2-Enter the following to make it executable:

    > chmod +x join_mapper.py

    > chmod +x join_reducer.py

3- Enter the following to see what directory you are in so that file your data and functions accordingly:

    > pwd

4- Create some data:

    > python make_join2data.py y 1000 13 > join2_gennumA.txt
    > python make_join2data.py y 2000 17 > join2_gennumB.txt
    > python make_join2data.py y 3000 19 > join2_gennumC.txt
    > python make_join2data.py n 100  23 > join2_genchanA.txt
    > python make_join2data.py n 200  19 > join2_genchanB.txt
    > python make_join2data.py n 300  37 > join2_genchanC.txt
    

5- Create a directory on the HDFS file system:

    > hdfs dfs -mkdir /user/your_working_directory__to_hdfs_file_system/input

6- Copy the files from local filesystem to the HDFS filesystem:

    > hdfs dfs -put /your_working_directory/join2_gennumA.txt /user/your_working_directory_to_hdfs_file_system/input
    > hdfs dfs -put /your_working_directory/join2_gennumB.txt /user/your_working_directory_to_hdfs_file_system/input
    > hdfs dfs -put /your_working_directory/join2_gennumC.txt /user/your_working_directory_to_hdfs_file_system/input
    > hdfs dfs -put /your_working_directory/join2_genchanA.txt /user/your_working_directory_to_hdfs_file_system/input
    > hdfs dfs -put /your_working_directory/join2_genchanB.txt /user/your_working_directory_to_hdfs_file_system/input
    > hdfs dfs -put /your_working_directory/join2_genchanC.txt /user/your_working_directory_to_hdfs_file_system/input

7- You can check your files on HDFS by following command: You should see 6 files.

    > hdfs dfs -ls /user/your_working_directory_to_hdfs_file_system/input

8- Run the Hadoop WordCount:

    > hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/your_working_directory_to_hdfs_file_system/input -output /user/your_working_directory_to_hdfs_file_system/output_new -mapper /your_working_directory/join_mapper.py -reducer /your_working_directory/join_reducer.py

9- You can see the output directory by first command and check out the contents by second command:

    > hdfs dfs -ls /user/your_working_directory_to_hdfs_file_system/output_new

    > hdfs dfs -cat /user/your_working_directory_to_hdfs_file_system/output_new/part-00000

10- You can get the output file from this run.

    > hdfs dfs -getmerge /user/your_working_directory_to_hdfs_file_system/output_new_0/* join_num0_output.txt

11- For other configuration you can set number of reduce task to be n by adding "-numReduceTask n" line to your run hadoop command (8th step). 
 
 
