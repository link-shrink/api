import firestoreDB
import validator


async def post_data(long_link: str, short_link: str):
    if not validator.valid_link(long_link):
        return {"Error": "Invalid URL"}

    data = {"short_link": short_link, "long_link": long_link}

    await firestoreDB.save_firestore("links", short_link, data)
    return data
