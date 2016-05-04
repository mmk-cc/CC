from flask import url_for
from app import db

class ConcertInfo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	mainArtist = db.Column(db.String(1024))
	instrument = db.Column(db.String(1024))
	accompanyingArtists = db.Column(db.String(1024))
	festival = db.Column(db.String(1024))
	timestamp = db.Column(db.DateTime)
	auditorium = db.Column(db.String(1024))
	address = db.Column(db.String(1024))
	city = db.Column(db.String(1024))
	state = db.Column(db.String(1024))
	country = db.Column(db.String(1024))
	url = db.Column(db.String(1024))
	contactEmail = db.Column(db.String(1024))
	genre = db.Column(db.String(1024))
 
	def __init__(self, mainArtist, instrument, accompanyingArtists, festival, timestamp, auditorium, address, city, state, country, url, contactEmail, genre):
		self.mainArtist = mainArtist
		self.instrument = instrument
		self.accompanyingArtists = accompanyingArtists
		self.festival = festival
		self.timestamp = timestamp
		self.auditorium = auditorium
		self.address = address
		self.city = city
		self.state = state
		self.country = country
		self.url = url
		self.contactEmail = contactEmail
		self.genre = genre

	def toJSON(self):
		return { 
			'mainArtist': self.mainArtist,
			'instrument': self.instrument,
			'accompanyingArtists': self.accompanyingArtists,
			'festival': self.festival,
			#'timestamp': self.timestamp,
			'auditorium': self.auditorium, 
			'city': self.city,
			'state': self.state,
			'country': self.country,
			'contacturl': self.url,
			'contactEmail': self.contactEmail,
			'ConcertInfoURI': url_for('get_task', concert_id=self.id, _external = True),
			'Genre': self.genre
		 } 


