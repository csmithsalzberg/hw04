from pymongo import MongoClient

def printstuff(ret):
    for re in ret:
        print re


c = MongoClient('lisa.stuy.edu')
coll = c.test
rests = coll.restaurants


def allBoro(boro):
    ret = rests.find({'borough': boro })
    printstuff(ret)
'''
allBoro('Queens')
''' 
def allZip(zipe):
    ret = rests.find({'address.zipcode': zipe })
    printstuff(ret)
'''
allZip('11373')
'''
def zg(zipe, grade):
    #ret = rests.find( {'address.zipcode': zipe , 'grades.grade':grade} )
    ret = rests.find({ '$and': [ {'address.zipcode': zipe},{'grades.grade':grade} ] })
    printstuff(ret)
'''
zg('11373','A')
'''

def zs(zipe, score):
    #ret = rests.find( {'address.zipcode': zipe , 'grades.grade':grade} )
    ret = rests.find({ '$and': [ {'address.zipcode': zipe}, {'grades.score': { '$lt' : score } } ] } )
    printstuff(ret)

zs('11378',12)


