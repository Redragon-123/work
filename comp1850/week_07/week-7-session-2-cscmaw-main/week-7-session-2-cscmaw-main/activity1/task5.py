class Movie:
    def __init__(self, title, director, year, genre, duration):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}, {self.genre}, {self.duration} mins"
    def __repr__(self): 
        return f"Movie(title='{self.title}', director='{self.director}', year={self.year}, genre='{self.genre}', duration={self.duration})" 
movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)
print(str(movie))
print(repr(movie))

# Define the __str__ and __repr__ in the following format:
# (1) __str__: Inception (2010), directed by Christopher Nolan, Sci-Fi, 148 mins
# (2) __repr__: Movie(title='Inception', director='Christopher Nolan', year=2010, genre='Sci-Fi', duration=148)
