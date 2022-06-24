# Deposit Serializers

def depositObject(item) -> dict:
    return {
        "id": str(item["_id"]),
        "bank_id": item["bank_id"],
        "currency": item["currency"],
        "amount": item["amount"],
        "reference": item["reference"],
        "status": item["status"]
    }


def depositsEntity(entity) -> list:
    return [depositObject(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
