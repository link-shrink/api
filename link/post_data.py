import firestoreDB
import validator
import milestones


async def post_data(original_link: str, link_id: str):
    if not validator.valid_link(original_link):
        return {"Error": "Invalid URL"}

    data = {"link_id": link_id, "original_link": original_link}

    await milestones.increase_quantity()
    await milestones.increase_short_length(f"keskn.uz/{link_id}")
    await milestones.increase_original_length(original_link)
    await firestoreDB.save_firestore("links", link_id, data)

    return data
