from firebase_admin import firestore
from .init_firestore import db


async def increase_firestore(field: str, quantity: int):
    doc_ref = db.collection("milestones").document("links")
    doc_ref.update({field: firestore.Increment(quantity)})
