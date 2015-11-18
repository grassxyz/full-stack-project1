"""
    Entertainment Center class

    This class is created for Full Stack Developer P1 Project and is used to
    launch a webpage which shows a few movies with links to the respective
    trailer

    :copyright: (c) 2015 by Andy Suen
"""


import fresh_tomatoes
import media

# This creates 3 movie objects
frozen = media.Movie("Frozen",
	                 "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1__SX1355_SY904_.jpg",
	                 "https://www.youtube.com/watch?v=TbQm5doF_Uc",
	                 2013)

ratatouille = media.Movie("Ratatouille",
	                      "http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1__SX1355_SY904_.jpg",
	                      "https://www.youtube.com/watch?v=KQUpZqshj7M",
	                      2007)

finding_nemo = media.Movie("Finding Nemo",
	                       "http://ia.media-imdb.com/images/M/MV5BMTY1MTg1NDAxOV5BMl5BanBnXkFtZTcwMjg1MDI5Nw@@._V1__SX1355_SY904_.jpg",
	                       "https://www.youtube.com/watch?v=2zLkasScy7A",
	                       2012)

# This initialize the list and put all movies into the list
movie_list = []
movie_list.append(frozen)
movie_list.append(ratatouille)
movie_list.append(finding_nemo)

# This call the provided program to launch a webpage
fresh_tomatoes.open_movies_page(movie_list)
