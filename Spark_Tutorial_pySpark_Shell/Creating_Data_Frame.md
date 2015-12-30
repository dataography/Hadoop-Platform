
#In this File, we will learn how to create data frame step by step, and perform some basic transformation


Lets a create a data frame of Directors

    > Movies = sc.parallelize([
      ["Naked", 1994, "Mike Leigh", "Comedy, Drama",7.9, 0],
      ["12 Angry Man", 1957,"Sidney Lumet", "Crime, Drama", 8.9, 3],
      ["Stalker", 1972,"Andrei Tarkovsky", "Sci-Fi, Drama", 8.2, 0],
      ["Seven Samurai", 1954,"Akira Kurosawa", "Comedy, Drama", 8.7, 2],
      ["One Flew Over the Cuckoo's Nest", 1975,"Milos Forman", "Comedy, Drama", 8.7, 5],
      ["Modern Times", 1936,"Charles Chaplin","Comedy, Drama", 8.6, 0]])

Lets derive mean of a 6 th column which is imbd score.

    > def extract_imdb_score(row):
             return row[4]
        
    > Movies.map(extract_imdb_score).mean()
    
    output: 8.5
        
Similarly you can derive # GROUP OF A COLUMN #  
    
    > def extract_genre_and_director(row):
          return (row[3],row[2])
    
    > Movies.map(extract_genre_and_director).collect()
    
    out[]: 
    [('Comedy, Drama', 'Mike Leigh'),
     ('Crime, Drama', 'Sidney Lumet'),
     ('Sci-Fi, Drama', 'Andrei Tarkovsky'),
     ('Comedy, Drama', 'Akira Kurosawa'),
     ('Comedy, Drama', 'Milos Forman'),
     ('Comedy, Drama', 'Charles Chaplin')]
     
we could also name this table by calling transformation as follow, and then call by collect() method

    > genre_and_director_RDD = Movies.map(extract_genre_and_director)
    > genre_and_director_RDD.collect()
    
We can GRUOP BY A COLUMN as follow. For simplicity, lets create new table of genre and imdb score.

    > def extract_genre_and_score(row):
          return (row[3], row[4])
    
    > genre_score_RDD = Movies.map(extract_genre_and_score)
    > genre_score_RDD.collect()
    
    out[]:
    [('Comedy, Drama', 7.9000000000000004),
     ('Crime, Drama', 8.9000000000000004),
     ('Sci-Fi, Drama', 8.1999999999999993),
     ('Comedy, Drama', 8.6999999999999993),
     ('Comedy, Drama', 8.6999999999999993),
     ('Comedy, Drama', 8.5999999999999996)]
     
Next lets find the max score for each genre. In spark language: max and reduceByKey() methods are in action

    > genre_score_RDD.reduceByKey(max).collect()
    
    out[]:
    [('Comedy, Drama', 8.6999999999999993),
     ('Sci-Fi, Drama', 8.1999999999999993),
     ('Crime, Drama', 8.9000000000000004)]
     
Similarly we can take min of the score for each genre by min and reduceByKey() methods
   
    >genre_score_RDD.reduceByKey(min).collect()
    
Now lets give a name for each column of our Movies table using sqlCtx.createDataFrame(..) and see our frame by show()

    > Movies_df = sqlCtx.createDataFrame(Movies,["movie","year","director","genre","imdb score", "#of nomination for 0scar"])
    
    > Movies_df.show() 
    
    out[]: 
          +--------------------+----+----------------+-------------+----------+------------------------+
          |               movie|year|        director|        genre|imdb score|#of nomination for oscar|
          +--------------------+----+----------------+-------------+----------+------------------------+
          |               Naked|1994|      Mike Leigh|Comedy, Drama|       7.9|                       0|
          |        12 Angry Man|1957|    Sidney Lumet| Crime, Drama|       8.9|                       3|
          |             Stalker|1972|Andrei Tarkovsky|Sci-Fi, Drama|       8.2|                       0|
          |       Seven Samurai|1954|  Akira Kurosawa|Comedy, Drama|       8.7|                       2|
          |One Flew Over the...|1975|    Milos Forman|Comedy, Drama|       8.7|                       5|
          |        Modern Times|1936| Charles Chaplin|Comedy, Drama|       8.6|                       0|
          +--------------------+----+----------------+-------------+----------+------------------------+

     > Movies_df.printSchema()
     
     out[]:
     
     root
       |-- movie: string (nullable = true)
       |-- year: long (nullable = true)
       |-- director: string (nullable = true)
       |-- genre: string (nullable = true)
       |-- imdb score: double (nullable = true)
       |-- #of nomination for oscar: long (nullable = true)
    
    
