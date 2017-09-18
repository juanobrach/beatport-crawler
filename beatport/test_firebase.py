import pyrebase
from fbconfig import *

firebase = pyrebase.initialize_app(config)
# Get a reference to the database service
db = firebase.database()
track = db.child("tracks").order_by_child('name').start_at('gil').limit_to_first(1).get()
print(track.val())