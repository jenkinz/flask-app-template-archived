from flask import Flask
from flask import jsonify
from flask import request
from flask_restful import abort
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    """Hello world example"""

    def get(self):
        return {"hello": "world"}


movies = [
    {
        "name": "Terminator 2: Judgment Day",
        "cast": [
            "Arnold Schwarzenegger",
            "Linda Hamilton",
            "Joe Morton",
        ],
        "genres": ["Action", "Sci-Fi"],
    },
    {
        "name": "The Shawshank Redemption",
        "cast": [
            "Tim Robbins",
            "Morgan Freeman",
            "Bob Gunton",
            "William " "Sadler",
        ],
        "genres": ["Drama"],
    },
]


def abort_if_movie_doesnt_exist(movie_id):
    """Check if movie_id is valid, and abort the request if invalid."""
    if movie_id >= len(movies):
        abort(404, message="Movie {} doesn't exist".format(movie_id))


class Movies(Resource):
    """Get a list of all movies, or POST to add new movies."""

    def get(self):
        """Return a list of all movies."""
        return jsonify(movies)

    def post(self):
        """Create a movie."""
        movie = request.get_json()
        movies.append(movie)
        return {"id": len(movies) - 1}, 201  # 201 CREATED (success)


class Movie(Resource):
    """Get a single movie, update a movie or delete a movie."""

    def get(self, movie_id):
        """Get a single movie."""
        abort_if_movie_doesnt_exist(movie_id)
        return jsonify(movies[movie_id])

    def put(self, movie_id):
        """Update a movie."""
        abort_if_movie_doesnt_exist(movie_id)
        movie = request.get_json()
        movies[movie_id] = movie
        return jsonify(movies[movie_id])

    def delete(self, movie_id):
        """Delete a movie."""
        abort_if_movie_doesnt_exist(movie_id)
        movies.pop(movie_id)
        return "", 200


api.add_resource(HelloWorld, "/")
api.add_resource(Movies, "/movies")
api.add_resource(Movie, "/movies/<int:movie_id>")


if __name__ == "__main__":
    app.run()
