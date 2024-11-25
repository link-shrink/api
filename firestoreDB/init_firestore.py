import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import json

load_dotenv()

firebase_json = os.getenv('FIREBASE_INIT')
cred = credentials.Certificate(json.loads(firebase_json))

firebase_admin.initialize_app(cred)

db = firestore.client()
