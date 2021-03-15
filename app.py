from flask import Flask
from flask import jsonify

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
    return jsonify(movie_entries)


app.run()
