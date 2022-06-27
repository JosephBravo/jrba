'''Withdraw Serializers'''

def withdrawObject(item) -> dict:
    return {
        "id": str(item["_id"]),
        "account_id": item["account_id"],
        "currency": item["currency"],
        "amount": item["amount"],
        "bank_data": item["bank_data"],
        "redirect_uri": item["redirect_uri"],
        "in_review": item["in_review"]
    }

def withdrawsEntity(entity) -> list:
    return [withdrawObject(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
