from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')
coll = c.test
rests = coll.restaurants


def allBoro(boro):
    ret = rests.find({'borough': boro })
    return ret;

ree = allBoro('Queens')
for re in ree:
    print re;
