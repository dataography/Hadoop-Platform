After you bundled your wordCount java class as jar file.
Change directory where the jar file is located:
$cd Dropbox/workspaceEE/WordCountJob/

Create some file:
$ cat > file.txt
sen sev seni seveni seni seven de sevsin seni 
and cmnd + d to save and exit alternatively
$ vi file.txt 
and enter 'i' and insert what ever you want, then esc+:+qw to save and quit


Lets first make directory
$mkdir input_file

Next put file.txt as an hdfs  format
$ hadoop fs -put file.txt input_file/file.txt

Next run tha hadoop job
$hadoop jar wordcount.jar WordCount input_file/file.txt wordcount_output

Now you can see your result goin into directory wordcount_output
$ cd wordcount_output
$ vi part-00000
