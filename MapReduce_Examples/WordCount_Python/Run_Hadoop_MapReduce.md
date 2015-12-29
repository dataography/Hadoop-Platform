
1- Type following commands in terminal and copy-past or directly download the wordcount_mapper.py  and wordcount_reducer.py 

    > gedit wordcount_mapper.py

    > gedit wordcount_reducer.py

2-Enter the following to make it executable:

    > chmod +x wordcount_mapper.py

    > chmod +x wordcount_reducer.py

3- Enter the following to see what directory you are in so that file your data and functions accordingly:

    > pwd

4- Create some data:

    > echo "A long time ago in a galaxy far far away" > /your_working_directory/testfile1

    > echo "Another episode of Star Wars" > /your_working_directory/testfile2

5- Create a directory on the HDFS file system (if already exists that’s OK):

    > hdfs dfs -mkdir /user/your_working_directory__to_hdfs_file_system/input

6- Copy the files from local filesystem to the HDFS filesystem:

    > hdfs dfs -put /your_working_directory/testfile1 /user/your_working_directory_to_hdfs_file_system/input

    > hdfs dfs -put /your_working_directory/testfile2 /user/your_working_directory_to_hdfs_file_system/input

7- You can check your files on HDFS by following command:

    > hdfs dfs -ls /user/your_working_directory_to_hdfs_file_system/input

8- Run the Hadoop WordCount:

    > hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/your_working_directory_to_hdfs_file_system/input -output /user/your_working_directory_to_hdfs_file_system/output_new -mapper /your_working_directory/wordcount_mapper.py -reducer /your_working_directory/wordcount_reducer.py

9- You can see the output directory by first command and check out the contents by second command:

    > hdfs dfs -ls /user/your_working_directory_to_hdfs_file_system/output_new

    > hdfs dfs -cat /user/your_working_directory_to_hdfs_file_system/output_new/part-00000

10- You can get the output file from this run.

    > hdfs dfs -getmerge /user/your_working_directory_to_hdfs_file_system/output_new_0/* wordcount_num0_output.txt

11- For other configuration you can set number of reduce task to be n by adding "-numReduceTask n" line to your run hadoop command (8th step). 
