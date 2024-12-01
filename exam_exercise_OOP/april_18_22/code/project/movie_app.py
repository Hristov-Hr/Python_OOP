from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        try:
            next(filter(lambda x: x.username == username, self.users_collection))
            raise Exception("User already exists!")
        except StopIteration:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda x: x.username == username, self.users_collection))

            if movie.owner.username != user.username:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")

            if movie in self.movies_collection:
                raise Exception("Movie already added to the collection!")

        except StopIteration:
            raise Exception("This user does not exist!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = [m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]
        return "\n".join(result)

    def __str__(self):
        result = [f"All users: {', '.join(u.username for u in self.users_collection) if self.users_collection else 'No users.'}", f"All movies: {', '.join(m.title for m in self.movies_collection) if self.movies_collection else 'No movies.'}"]

        return "\n".join(result)


