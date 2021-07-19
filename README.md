# imdb-api
This api is deployed at DETA.
Request:
https://gqycaf.deta.dev/get-random-movie/{movie_rating}?numVotes={number_of_votes}<br /> 
Here you will be given a movie info with rating  greater than or equal to movie_rating and number of ratings greater than or equal to number_of_votes.<br /> 
Here query parameter numVotes is optional.<br /> 
So, https://gqycaf.deta.dev/get-random-movie/{movie_rating} will also work fine.<br /> 
Examples:<br /> 
https://gqycaf.deta.dev/get-random-movie/8?numVotes=6000 <br /> 
gave {"link":"https://www.imdb.com/title/tt2384811","averageRating":8.4,"numVotes":42819}<br /> 
https://gqycaf.deta.dev/get-random-movie/5<br /> 
gave {"link":"https://www.imdb.com/title/tt1646926","averageRating":5.1,"numVotes":10584}<br /> 
Note:<br /> 
same link may give a different movie each time since, selecting a movie is completely random<br /> 
Information courtesy of IMDb (http://www.imdb.com).<br /> 
Dataset details:https://www.imdb.com/interfaces/ <br /> 
Data downloaded from:https://datasets.imdbws.com/ <br /> 
