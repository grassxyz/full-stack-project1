"""
    Movie class

    This movie class is created for Full Stack Developer P1 Project

    :copyright: (c) 2015 by Andy Suen
"""


class Movie():

    def __init__(self, movie_title, movie_poster_image_url, movie_trailer_url, movie_release_date):
    	self.title = movie_title
    	self.poster_image_url = movie_poster_image_url
    	self.trailer_youtube_url = movie_trailer_url
    	self.release_date = movie_release_date    # an extra property defined for this Movie class


