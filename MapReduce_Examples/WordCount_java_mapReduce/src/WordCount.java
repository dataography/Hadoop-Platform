import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.io.*;
import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.util.*;

public class WordCount extends Configured implements Tool {

	@Override
	// this method is an abstract method of the Configured class. must be
	// implemented.
	// takes 2 arguments which are namely input and output directory.
	public int run(String[] args) throws Exception {
		if (args.length < 2) {
			System.out.println("Please give input and ouput directory");
			return -1;
		}
		// We create a new job configuration having WordCount class as an
		// argument
		JobConf conf = new JobConf(WordCount.class);

		// We need to define the input and output format using
		// FileInputFormat, FileOutputFormat class end setInputPath(s) methods
		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		//Need to set mapper and reducer classes
		conf.setMapperClass(WordMapper.class);
		conf.setReducerClass(WordReducer.class);
        
		//Next need to introduce mapper's outputs type (key type and value type)
		//mapper reads the hdfs file line by line and prododuce key and values -> then it will be sorted and distributed to reducer.
		conf.setMapOutputKeyClass(Text.class);
		conf.setMapOutputValueClass(IntWritable.class);
		
		
		//Next we set our final output type
		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(IntWritable.class);

		//from JobClient class we run the runJob method and give the our configuration conf as an argument.
		JobClient.runJob(conf);
		return 0;
	}

	public static void main(String args[]) throws Exception {
		
		int exitCode = ToolRunner.run(new WordCount(), args);
		System.exit(exitCode);
	}

}
