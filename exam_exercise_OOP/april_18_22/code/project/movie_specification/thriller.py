from project.movie_specification.movie import Movie


class Thriller(Movie):

    VALID_AGE = 16
    GENRE = "Thriller"

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"