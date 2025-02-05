import firestoreDB


async def increase_quantity() -> None:
    await firestoreDB.increase_firestore("quantity", 1)
