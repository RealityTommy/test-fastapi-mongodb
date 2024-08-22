import json
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth, firestore
from app.config.firebase.config import firebaseConfig

# Firebase service account key
serviceAccountKeyFile = open("app/config/firebase/serviceAccountKey.json")
serviceAccountKey = json.load(serviceAccountKeyFile)

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(serviceAccountKey)
    firebase_admin.initialize_app(cred)

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Initialize Firestore
db = firestore.client()