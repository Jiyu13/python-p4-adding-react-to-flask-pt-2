from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/movies', methods=["GET"])
def movies():
    # response_dict = {"text": "Movies will go here"}
    # return make_response(jsonify(response_dict), 200)

    if request.method == 'GET':
        movies = Movie.query.all()
        movies_list_dict = jsonify([movie.to_dict() for movie in movies])
        return make_response(movies_list_dict, 200)
    
    response_body = {"text": "Method Not Allowed"}
    return make_response(jsonify(response_body), 405)

if __name__ == "__main__":
    app.run(port=5555)