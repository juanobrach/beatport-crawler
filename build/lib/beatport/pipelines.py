# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pyrebase


class JsonWriterPipeline(object):

	def process_item(self, item, spider):
		config = {
		  "apiKey": "AIzaSyCYCNVK5Us5s0D_UkJfcVWIl5NyAu8ofHo",
		  "authDomain": "beatport-772ec.firebaseapp.com",
		  "databaseURL": "https://beatport-772ec.firebaseio.com/",
		  "storageBucket": "beatport-772ec.appspot.com"
		}
		firebase = pyrebase.initialize_app(config)
		# Get a reference to the database service
		db = firebase.database()
		
		# data to save
		# Pass the user's idToken to the push method
		for key, value in item.items():
			if key == 'name':
				name = value
				track = db.child("tracks").order_by_child('name').equal_to(str(name)).get()
				try: 
					print(track.val())
				except IndexError:
					print( "No duplicated, do it." )
					data = item
					results = db.child("tracks").push(data)
		return item