from flask import Flask, render_template, redirect, url_for, request, flash, url_for
from models.listing import Listing
from pymongo import MongoClient
import requests

list_coll = MongoClient('localhost:27017').ffs.listings
app = Flask(__name__)
HOME = 'http://gatechffs.com'

@app.route('/')
def landing():
	return render_template('index.html')

@app.route('/listing',methods=["GET","POST"])
def listing():
	if request.method == 'GET':
		lid = request.args.get('listId')
		if not lid:
			return render_template('notfound.html')
		listing = list_coll.find_one(dict(_id=lid))
		if not listing:
			return render_template('notfound.html')
		if 'cllink' in listing and listing['cllink']:
			return render_template('showcllisting.html',
			listing=listing)
		else:
			return render_template('showlisting.html',
			listing=listing)
		
	elif request.method == 'POST':
		# TODO form validation
		# title and desc are required.
		# one of email and phone is required.
		lst = Listing(
			title=request.form.get('title'),
			desc=request.form.get('desc'),
			price=request.form.get('price'),
			email=request.form.get('email'),
			phone=request.form.get('phone'),
			cllink=request.form.get('cllink')
			)
		lst.save(list_coll)
		if lst.cllink:
			return render_template('showcllisting.html',
			listing=lst)
		else:
			return render_template('showlisting.html',
			listing=lst)

if __name__ == '__main__':
	app.debug = True
	app.run('0.0.0.0',80)
