from project.movie_specification.movie import Movie


class Action(Movie):

    VALID_AGE = 12
    GENRE = "Action"

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"