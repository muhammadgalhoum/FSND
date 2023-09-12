from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


Role = db.Table('Role',
    db.Column('movie_id', db.Integer, db.ForeignKey('Movies.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('Actors.id'), primary_key=True),
)



class Movie(db.Model):  
	__tablename__ = 'Movies'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	release_date = db.Column(db.Date)
	actors = db.relationship('Actor', secondary=Role, backref=db.backref('movies', lazy=True))

	def __init__(self, title, release_date):
		self.title = title
		self.release_date = release_date

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
		'id': self.id,
		'title': self.title,
		'release_date': self.release_date,
		'actors': [actor.name for actor in self.actors]
  	}

class Actor(db.Model):
	__tablename__ = 'Actors'
		
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	age = db.Column(db.Integer)
	gender = db.Column(db.String)
	
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
		
	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()
		
	def format(self):
		return {
		'id': self.id,
		'name': self.name,
		'age': self.age,
		'gender': self.gender
		}