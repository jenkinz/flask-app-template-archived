from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


movie_entries = [
    {
        "name": "Terminator 2: Judgment Day",
        "cast": ["Arnold Schwarzenegger", "Linda Hamilton", "Joe Morton"],
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


@app.route("/")
@app.route("/movies")
def movies():
    """Return all movie entries."""
    return jsonify(movie_entries)


@app.route("/movies", methods=["POST"])
def add_movie():
    """Add a movie entry."""
    movie = request.get_json()
    movie_entries.append(movie)
    return {"id": len(movie_entries)}, 201  # 201 CREATED (success)


@app.route("/movies/<int:index>", methods=["PUT"])
def update_movie(index):
    """Update a movie entry."""
    movie = request.get_json()
    movie_entries[index] = movie
    return jsonify(movie_entries[index])


@app.route("/movies/<int:index>", methods=["DELETE"])
def delete_movie(index):
    """Delete a movie entry."""
    if index < len(movie_entries):
        movie_entries.pop(index)
        return "None", 200
    else:
        return "Not Found", 404


app.run()
