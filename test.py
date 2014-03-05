from config import db, PORT
from models import *
import json
import urllib2

BASE_URL = "http://127.0.0.1:" + str(PORT) + "/api/"

def insert_test_users():
	user = User("testing@test.com", "password", "alan", "luong")
	db.session.add(user)
	user = User("bobdole@gmail.com", "asdf", "bob", "dole")
	db.session.add(user)
	user = User("alice123@yahoo.com", "fdsa", "alice", "dole")
	db.session.add(user)
	db.session.commit()

def insert_test_ads():
	ad = Ad("testing@test.com", 23.20, "a bag of bananas")
	db.session.add(ad)
	ad = Ad("bobdole@gmail.com", 99.99, "a car")
	db.session.add(ad)
	ad = Ad("bobdole@gmail.com", 0, "this is a test ad")
	db.session.add(ad)
	db.session.commit()

def post(url, data):
	response = ""
	req = urllib2.Request(url, data, {"Content-Type": "application/json"})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	return response
