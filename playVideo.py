class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

movie = Movie_MP4(r"C:\My Documents\My Videos\Heres_a_file.mp4")
if raw_input("Press enter to play, anything else to exit") == '':
    movie.play()
