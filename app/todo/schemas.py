def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"],
        "firebase_uid": todo["firebase_uid"]
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]