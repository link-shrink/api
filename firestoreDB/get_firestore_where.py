from .init_firestore import db


async def get_firestore_where(collection: str, key: str, value: any):
    docs = db.collection(collection).where(key, "==", value).stream()

    res = []
    for doc in docs:
        res.append(doc.to_dict())

    return res
