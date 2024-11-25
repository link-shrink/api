import firestoreDB
import validator


async def post_data(original_link: str, link_id: str):
    if not validator.valid_link(original_link):
        return {"Error": "Invalid URL"}

    data = {"link_id": link_id, "original_link": original_link}

    await firestoreDB.save_firestore("links", link_id, data)
    return data
