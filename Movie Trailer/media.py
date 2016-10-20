import webbrowser

class Movie():
    """
        This Class defines the movie and its attributes.
         It contains attributes like movie title, movie story, poster image and youtube trailer
    """

    def __init__(self, movie_title, movie_story, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


