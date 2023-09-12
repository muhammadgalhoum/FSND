import json
import unittest

from app import create_app
from models import db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""

        self.app = create_app(test_config={'TEST_DATABASE_URL': "postgresql://postgres:123456@localhost:5432/capstone_test"})
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()
        
        self.new_movie = {
            "title": "Movie Title",
            "release_date": "2023-09-10",
            "actors" : [1, 2],
        }
        
        self.new_actor = {
            "name": "John Doe",
            "age": 30,
            "gender" : "male",
        }
    
    
    def tearDown(self):
        """Executed after reach test"""
        pass
        
    def test_create_new_movie(self):
        res = self.client().post("/movies", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["movies"]))

    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().post("/movies/1", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    def test_update_movie_title(self):
        with self.app.app_context():
            res = self.client().patch("/movies/1", json={"title": "Movie Title"})
            data = json.loads(res.data)
            movie = Movie.query.filter(Movie.id == 1).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(movie.format()["title"], "Movie Title")

    def test_400_for_failed_update(self):
        with self.app.app_context():
            res = self.client().patch("/movies/1")
            data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_delete_movie(self):
        with self.app.app_context():
            res = self.client().delete("/movies/1")
            data = json.loads(res.data)

            movie = Movie.query.filter(Movie.id == 1).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["deleted"], 1)
            self.assertTrue(len(data["movies"]))
            self.assertTrue(data["total_movies"])
            self.assertEqual(movie, None)

    def test_422_if_movie_does_not_exist(self):
            res = self.client().delete("/movies/1000")
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data["success"], False)
            self.assertEqual(data["message"], "unprocessable") 
            
              
    def test_create_new_actor(self):
        res = self.client().post("/actors", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["actors"]))

    def test_405_if_actor_creation_not_allowed(self):
        res = self.client().post("/actors/1", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    def test_update_actor_age(self):
        with self.app.app_context():
            res = self.client().patch("/actors/1", json={"age": 25})
            data = json.loads(res.data)
            actor = Actor.query.filter(Actor.id == 1).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(actor.format()["age"], 25)

    def test_400_for_failed_update(self):
        with self.app.app_context():
            res = self.client().patch("/actors/1")
            data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_delete_actor(self):
        with self.app.app_context():
            res = self.client().delete("/actors/1")
            data = json.loads(res.data)

            actor = Actor.query.filter(Actor.id == 1).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["deleted"], 1)
            self.assertTrue(len(data["actors"]))
            self.assertTrue(data["total_actors"])
            self.assertEqual(actor, None)

    def test_422_if_actor_does_not_exist(self):
            res = self.client().delete("/actors/1000")
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data["success"], False)
            self.assertEqual(data["message"], "unprocessable")   

if __name__ == "__main__":
  unittest.main()