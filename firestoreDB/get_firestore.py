from .init_firestore import db


async def get_firestore(collection: str, doc_id: str):
    doc_ref = db.collection(collection).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()

    return None
