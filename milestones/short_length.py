import firestoreDB


async def increase_short_length(short_link: str) -> None:
    await firestoreDB.increase_firestore("short_length", len(short_link))
