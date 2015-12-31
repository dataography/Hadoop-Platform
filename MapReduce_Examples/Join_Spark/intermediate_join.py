# This is the second assignment in Coursera Class- Hadoop Platform and Application Framework. 
# Code is written in pySpark shell in Cloudera Virtual Machine. 
# Aim is to find the total views for the channel BAT given the tables: <shows, views> and <views, channels>
#load the data of shows and views.
in[]: show_views_file = sc.textFile("input/join2_gennum?.txt")
in[]: show_views_file.take(3)
out[]: 
[u'Hourly_Sports,21', u'PostModern_Show,38', u'Surreal_News,73']

in[]: def split_show_views(line):
           temp = line.split(",")
           show = temp[0]
           views = temp[1]
           return(show,views)

in[]: show_views = show_views_file.map(split_show_views)
in[]: show_views.take(3)
out[]: 
[(u'Hourly_Sports', u'21'),
 (u'PostModern_Show', u'38'),
 (u'Surreal_News', u'73')]
#load the data of shows and channels.
in[]: show_channel_file = sc.textFile("input/join2_genchan?.txt")
in[]: show_channel_file.take(3) 
out[]: 
[u'Hourly_Sports,DEF', u'Baked_News,BAT', u'PostModern_Talking,XYZ']


in[]: def split_show_channel(line):
          temp = line.split(",")
          show = temp[0]
          channel = temp[1]
          return (show,channel)

in[]: show_channel = show_channel_file.map(split_show_channel)
in[]: show_channel.take(3)
out[]: 
[(u'Hourly_Sports', u'DEF'),
 (u'Baked_News', u'BAT'),
 (u'PostModern_Talking', u'XYZ')]


in[]: joined_dataset = show_views.join(show_channel)
in[]: joined_dataset.take(3)
out[]: 
[(u'PostModern_Cooking', (u'1038', u'DEF')),
 (u'PostModern_Cooking', (u'1038', u'CNO')),
 (u'PostModern_Cooking', (u'1038', u'CNO'))]

in[]: def extract_channel_views(show_views_channel):
             channel = show_views_channel[1][1]
             views = show_views_channel[1][0]
             return (channel,views)

in[]: channel_views = joined_dataset.map(extract_channel_views)
in[]: channel_views.take(3)
out[]: 
[(u'DEF', u'1038'), (u'CNO', u'1038'), (u'CNO', u'1038')]

in[]: def BAT(pair):                                                     
          if (pair[0]=="BAT"):
              return True
in[]: def sum_counts(a,b): 
          return int(a) +int(b)

in[]: total_views_for_BAT=channel_views.reduceByKey(sum_counts).filter(BAT)
in[]: total_views_for_BAT.collect()
Out[]: 
[(u'BAT', ****141)]
# total views for Channel BAT is 7-digit number:  ****141
