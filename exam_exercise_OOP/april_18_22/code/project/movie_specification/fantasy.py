from project.movie_specification.movie import Movie


class Fantasy(Movie):

    VALID_AGE = 6
    GENRE = "Fantasy"

    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"