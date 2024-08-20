def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "firebase_uid": user["firebase_uid"]
    }

def list_serial(users) -> list:
    return [individual_serial(user) for user in users]