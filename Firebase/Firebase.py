import pyrebase
import os

# firebase API keys
config = {
  "apiKey": os.environ.get("REACT_APP_FIREBASE_API_KEY"),
  "authDomain": os.environ.get("REACT_APP_FIREBASE_AUTH_DOMAIN"), 
  "databaseURL": "https://home-automation-4ebbb-default-rtdb.asia-southeast1.firebasedatabase.app", 
  "storageBucket": os.environ.get("REACT_APP_FIREBASE_STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)
db = firebase.database() # realTime database

def get_control_functions(name):
    try:
        data = db.child(name).child("data").get().val()
        
        return data 
        
    except Exception as e:
        print(f"Error: {e}")
        return False
