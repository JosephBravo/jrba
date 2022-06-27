'''Account Serializers'''

def accountObject(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user": item["user"],
        "name": item["name"],
        "description": item["description"],
        "country": item["country"],
        "balances": item["balances"],
        "status": item["status"]
    }

def accountsEntity(entity) -> list:
    return [accountObject(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
