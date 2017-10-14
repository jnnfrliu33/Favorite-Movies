import webbrowser

class Movie():
    def __init__(self, title, synopsis, poster_image, trailer):
        """
        Initializes the movie instance
        Inputs: title, synopsis, poster image url and
                YouTube trailer url of the movie
        Output: None
        """
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer


    def show_trailer(self):
        """
        Opens the trailer of the movie in a browser
        Input: YouTube trailer url
        Output: None
        """
        webbrowser.open(self.trailer_youtube_url)
