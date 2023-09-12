import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import db, Movie, Actor
from auth.auth import AuthError, requires_auth

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)
  
  

def create_app(test_config=None):
	app = Flask(__name__)
  
	if test_config is not None:
		# Use the test database URL from the test configuration
		database_url = test_config['TEST_DATABASE_URL']
	else:
		# Use the development database URL as a default
		database_url = database_path
	
	app.config["SQLALCHEMY_DATABASE_URI"] = database_url
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	
	with app.app_context():
		db.init_app(app)
		db.create_all()
  
	CORS(app)
  
	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
		response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
		return response

	@app.route('/')
	def get_greeting():
		excited = os.environ['EXCITED']
		greeting = "Hello" 
		if excited == 'true': 
			greeting = greeting + "!!!!! You are doing great in this Udacity project."
		return greeting

	@app.route('/coolkids')
	def be_cool():
		return "Be cool, man, be coooool! You're almost a FSND grad!"

	@app.route('/movies')
	@requires_auth('get:movies')
	def retrieve_movies(jwt):
		selection = Movie.query.order_by(Movie.id).all()
		movies = [movie.format() for movie in selection]
    
		if len(movies) == 0:
			abort(404)
		
		return jsonify({
		'success': True,
		'movies': movies,
		'total_movies': len(Movie.query.all()),
		})
	
	@app.route('/movies/<int:movie_id>')
	@requires_auth('get:movies-detail')
	def get_specific_movie(jwt,movie_id):
		movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
		
		if movie is None:
			abort(404)
   
		else:
			return jsonify({
				'success': True,
				'movie': movie.format(),
			})
	
 
	@app.route("/movies", methods=["POST"])
	@requires_auth('post:movies')
	def create_movie(jwt):
		body = request.get_json()

		new_title = body.get("title", None)
		new_release_date = body.get("release_date", None)
		actor_ids = body.get("actor_ids", [])  # Use actor_ids to represent the list of actor IDs

		try:
			new_movie = Movie(
				title=new_title,
				release_date=new_release_date,
			)
			
			# Assign actors using their IDs
			new_movie.actors = [Actor.query.get(actor_id) for actor_id in actor_ids]

			new_movie.insert()

			selection = Movie.query.order_by(Movie.id).all()
			movies = [movie.format() for movie in selection]

			return jsonify(
				{
					"success": True,
					"created": new_movie.id,
					"movies": movies,
					"total_movies": len(Movie.query.all()),
				}
			)
		except:
			abort(422)


	@app.route("/movies/<int:movie_id>", methods=["PATCH"])
	@requires_auth('patch:movies')
	def update_movie(jwt,movie_id):
		try:
			body = request.get_json()
			movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

			if movie is None:
				abort(404)
			else:
				new_title = body.get("title", None)
				new_release_date = body.get("release_date", None)
				actor_ids = body.get("actor_ids", [])  # Use actor_ids to represent the list of actor IDs

				if new_title is not None:
					movie.title = new_title
				if new_release_date is not None:
					movie.release_date = new_release_date

				# Retrieve the corresponding actor objects using their IDs
				actors = [Actor.query.get(actor_id) for actor_id in actor_ids]

				# Assign the actors to the movie
				movie.actors = actors

				movie.update()

				return jsonify({
					"id": movie_id,
					"success": True,
				})

		except:
			abort(400)


	@app.route("/movies/<int:movie_id>", methods=["DELETE"])
	@requires_auth('delete:movies')
	def delete_movie(jwt,movie_id):
		try:
			movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

			if movie is None:
				abort(404)
			
			movie.delete()
   
			selection = Movie.query.order_by(Movie.id).all()
			movies = [movie.format() for movie in selection]

			return jsonify(
				{
				"success": True,
				"deleted": movie_id,
				"movies": movies,
				"total_movies": len(Movie.query.all()),
				}
			)

		except:
			abort(422)
   
   
	@app.route('/actors')
	@requires_auth('get:actors')
	def retrieve_actors(jwt):
		selection = Actor.query.order_by(Actor.id).all()
		actors = [actor.format() for actor in selection]
    
		if len(actors) == 0:
			abort(404)
		
		return jsonify({
		'success': True,
		'actors': actors,
		'total_actors': len(Actor.query.all()),
		})
	
	@app.route('/actors/<int:actor_id>')
	@requires_auth('get:actors-detail')
	def get_specific_actor(jwt,actor_id):
		actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
		
		if actor is None:
			abort(404)
   
		else:
			return jsonify({
				'success': True,
				'actor': actor.format(),
			})
	
	@app.route("/actors", methods=["POST"])
	@requires_auth('post:actors')
	def create_actor(jwt):
		body = request.get_json()

		new_name = body.get("name", None)
		new_age = body.get("age", None)
		new_gender = body.get("gender", None)

		try:

			new_actor = Actor(
			name=new_name, 
			age=new_age, 
			gender=new_gender
			)
			
			new_actor.insert()

			selection = Actor.query.order_by(Actor.id).all()
			actors = [actor.format() for actor in selection]

			return jsonify(
				{
					"success": True,
					"created": new_actor.id,
					"actors": actors,
					"total_actors": len(Actor.query.all()),
				}
			)

		except:
			abort(422)
   
	@app.route("/actors/<int:actor_id>", methods=["PATCH"])
	@requires_auth('patch:actors')
	def update_actor(jwt,actor_id):
		try:
			body = request.get_json()
			actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
		
			if actor is None:
				abort(404)
			
			else:
				new_name = body.get("name", None)
				new_age = body.get("age", None)
				new_gender = body.get("gender", None)
				
				if new_name is not None:
					actor.name = new_name
				if new_age is not None:
					actor.age = int(new_age)
				if new_gender is not None:
					actor.actors = new_gender
				
				actor.update()
				
				return jsonify({
				"id": actor_id,
				"success": True,
				})
			
		except:
			abort(400)

	@app.route("/actors/<int:actor_id>", methods=["DELETE"])
	@requires_auth('delete:actors')
	def delete_actor(jwt,actor_id):
		try:
			actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

			if actor is None:
				abort(404)
			
			actor.delete()
   
			selection = Actor.query.order_by(Actor.id).all()
			actors = [actor.format() for actor in selection]

			return jsonify(
				{
				"success": True,
				"deleted": actor_id,
				"actors": actors,
				"total_actors": len(Actor.query.all()),
				}
			)

		except:
			abort(422)
   
   
	# Handling Errors
	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({
		"success": False,
		"error": 400,
		"message": "bad request"
		}), 400
	
	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
		"success": False,
		"error": 404,
		"message": "resource not found"
		}), 404
	
	@app.errorhandler(405)
	def not_allowed(error):
		return jsonify({
		"success": False,
		"error": 405,
		"message": "method not allowed"
		}), 405
	
	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
      }), 422
  
  
	return app


app = create_app()

if __name__ == '__main__':
    app.run()