import random
import string
import firestoreDB


def get_random_link(length=12):
    length = int(length)
    return "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length
        )
    )


async def generate_link_id(length=12, max_retries=10):
    for _ in range(max_retries):
        random_id = get_random_link(length)
        if not await firestoreDB.get_firestore("links", random_id):
            return {"ok": True, "link_id": random_id}

    return {"ok": False, "Error": "Couln't generate short link, try again."}
