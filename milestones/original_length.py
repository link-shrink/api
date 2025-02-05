import firestoreDB


async def increase_original_length(original_link: str) -> None:
    await firestoreDB.increase_firestore("original_length", len(original_link))
