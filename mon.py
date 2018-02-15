from pymongo import MongoClient
import json

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
'''
zs('11378',12)
'''

def bgs(boro, grade, score):
    ret = rests.find({ '$and': [ {'borough': boro }, {'grades.grade':grade}, {'grades.score': { '$lt' : score } } ] } )
    printstuff(ret)
    
#bgs("Queens","A",30)


with open('comets.json') as jfile:
    data = json.load(jfile)
    min=data[0]['year'][0:data[0]['year'].find('-')]
    print min
    for entry in data:
        if entry['year'][0:data[0]['year'].find('-')] < min:
            min = entry['year'][0:data[0]['year'].find('-')]
        print entry['year'][0:data[0]['year'].find('-')]
    print min
    #print data
#db.exceptForTheMongols.insert({})
