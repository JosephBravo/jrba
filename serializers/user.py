# User Serializer

def userObject(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user": item["user"],
        "name": item["name"],
        "surname": item["surname"],
        "second_surname": item["second_surname"],
        "password": item["password"],
        "active": item["active"],
        "role": item["role"],
        "college": item["college"],
        "created_at": item["created_at"]
    }


def usersEntity(entity) -> list:
    return [userObject(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
