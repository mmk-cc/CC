#! /usr/bin/python

import json
from flask import Flask, jsonify, abort, request, make_response, url_for, Response
from flask_restful import reqparse
from app import app, db
from app.models import ConcertInfo
from flask.ext.sqlalchemy import SQLAlchemy, orm
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/cc/api/v1.0/concerts', methods = ['GET'])
def get_concerts():
  x = []
  for i in db.session.query(ConcertInfo).all():
	x.append(i.toJSON())
  return jsonify({'concerts':x})

@app.route('/cc/api/v1.0/concerts/<int:concert_id>', methods = ['GET'])
def get_task(concert_id):
    cid = int(concert_id)
    x = []
    for i in db.session.query(ConcertInfo).filter_by(id=cid).all():
	x.append(i.toJSON())
    if len(x) == 0:
        abort(404)
    return jsonify({'concerts':x})

@app.route('/cc/api/v1.0/concerts/festival/<string:fest>', methods = ['GET'])
def get_fest(fest):
    x = []
    for i in db.session.query(ConcertInfo).filter_by(festival=fest).all():
	x.append(i.toJSON())
    if len(x) == 0:
        abort(404)
    return jsonify({'concerts':x})

@app.route('/cc/api/v1.0/concerts', methods = ['POST'])
def create_task():
    concertDatetime = request.form['mmddyyyy'] + ' ' + request.form['hh'] + ':' + request.form['mm'] + ':00' ;
    c = ConcertInfo (request.form['mainArtist'], request.form['instrument'], request.form['accompanyingArtists'], request.form['festival'],
                     concertDatetime, request.form['auditorium'], request.form['address'], request.form['city'], request.form['state'], 
                     request.form['country'], request.form['url'], request.form['contactEmail'], request.form['genre'])
  
    db.session.add(c)
    db.session.commit()
    return jsonify( { 'concerts': c.toJSON() } ), 201

@app.route('/cc/api/v1.0/concerts/<int:cid>/delete', methods = ['GET'])
def delete_concert(cid):
    x = []
    for i in db.session.query(ConcertInfo).filter_by(id=cid):
	db.session.delete(i)
    db.session.commit()
    return jsonify( { 'result': True } )
 
def makequerystring(arglist,param):
	return param + ' in (' + ','.join(("\""+i+"\"" for i in arglist)) + ')'

def makewhereclause(args, argsofinterest):
	whereclauses = [] 
	for i in argsofinterest:
		if args[i] != None: 
			whereclauses.append(makequerystring(args[i],i))
	whereclause = ' and '.join(whereclauses)
	return whereclause


@app.route('/cc/api/v1.0/concerts/search', methods = ['GET'])
def search_concert():
	searchables = [ 'mainartist', 'instrument', 'accompanyingartists', 'festival', 'auditorium', 'city', 'state', 'country', 'genre' ]
	parser = reqparse.RequestParser()
	for i in searchables:
		parser.add_argument(i, action='append')
	args = parser.parse_args()
	whereclause = makewhereclause(args, searchables)

    	x = []
    	for i in db.session.query(ConcertInfo).filter(text(whereclause)).all():
		x.append(i.toJSON())

	if len(x) == 0:
        	abort(404)
	
	return jsonify({'concerts':x})

def get_one_column(what, nameofwhat, by):
	c = []
	parser = reqparse.RequestParser()
	for b in by:
		parser.add_argument(b, action='append')
	args = parser.parse_args()
	whereclause = makewhereclause(args, by)

	for i in db.session.query(what).filter(text(whereclause)).distinct():
		c.append(i)
	return jsonify( { nameofwhat : c })

@app.route('/cc/api/v1.0/states', methods = ['GET'])
def get_state():
	return get_one_column(ConcertInfo.state, 'state', ['country'] )

@app.route('/cc/api/v1.0/cities', methods = ['GET'])
def get_city():
	return get_one_column(ConcertInfo.city, 'city', ['country', 'state'])


@app.route('/cc/api/v1.0/countries', methods = ['GET'])
def get_country():
	return get_one_column(ConcertInfo.country, 'country', [])


@app.route('/cc/api/v1.0/festivals', methods = ['GET'])
def get_festival():
	return get_one_column(ConcertInfo.festival, 'festival', [])

@app.route('/cc/api/v1.0/mainartists', methods = ['GET'])
def get_mainartist():
	return get_one_column(ConcertInfo.mainArtist, 'mainArtist', [])

@app.route('/cc/api/v1.0/instruments', methods = ['GET'])
def get_instruments():
	return get_one_column(ConcertInfo.instrument, 'instrument', [])

@app.route('/cc/api/v1.0/genres', methods = ['GET'])
def get_genres():
	return get_one_column(ConcertInfo.genre, 'genre', [])






