import pyrebase
from fbconfig import *

firebase = pyrebase.initialize_app(config)
# Get a reference to the database service
db = firebase.database()
track = db.child("tracks").order_by_child("name").equal_to("You Know What I'm Talking About").get()
try: 
	print(track.val())
except IndexError:
	print( "No duplicated, do it." )