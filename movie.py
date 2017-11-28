###############################################################################
# filename: movie.py
# description: This is the class file for the movie_project.py program
# Required Files: none
###############################################################################

import webbrowser

# Define the movie class
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating, length):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.length = length
