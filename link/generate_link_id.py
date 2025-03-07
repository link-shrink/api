import firestoreDB


async def generate_link_id():
    quantity = await firestoreDB.get_firestore("milestones", "links")
    unique_id = generate_unique_string(quantity["quantity"])

    if unique_id:
        return {"ok": True, "link_id": unique_id}

    return {"ok": False, "Error": "Couln't generate short link, try again."}


def generate_unique_string(num):
    result = ""
    base62 = "LtQSHIPTg73MiVdEyo1vRz6bZJAxuaeCGKWshmr45fqkFBn9Y0XljNcD2UwO8p"

    while num > 0:
        result = base62[num % 62] + result
        num //= 62

    return result.zfill(6)
