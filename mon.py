from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')
coll = c.test
rests = coll.restaurants


def allBoro(boro):
    ret = rests.find({'borough': boro })
    return ret;

bor = allBoro('Queens')
for re in bor:
    print re;
    
def allZip(zipe):
    ret = rests.find({'address.zipcode': zipe })
    return ret;

zips = allZip('11373')
for re in zips:
    print re;


