
from pymongo import MongoClient



def citiesQuery(mongoquery):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ


    cursor = db.cities.find({"name":mongoquery})

    return cursor;


def loginQuery(user,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"user":user.upper()})

    for u in cursor:
        if u.get("password") == hashPass:
            return True

    return False;

def registerQuery(user,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"user":user.upper()})

    for c in cursor:
        return False;

    result = db.users.insert(
            {
                "user":user.upper(),
                "password":hashPass
            })
    return True;


