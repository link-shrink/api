from .init_firestore import db


async def save_firestore(collection_name, doc_name, data):
    doc_ref = db.collection(collection_name).document(doc_name)
    doc_ref.set(data)
