import tweepy
import couchdb
import pycurl
import json


user = "admin"
password = "admin"
db_ip = '127.0.0.1'
couchserver = couchdb.Server('http://%s:%s@%s:5984/'% (user, password, db_ip))
auriandb = "population"
dbname = "starry_data"
# add the Aurian db population if not exists
if auriandb not in couchserver:
    # create db
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/%s?partitioned=true'% (user, password, db_ip, auriandb))
    crl.setopt(crl.UPLOAD, 1) 
    crl.perform()
    crl.close()
    # add data
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/%s/_bulk_docs'% (user, password, db_ip, auriandb))
    crl.setopt(pycurl.HTTPHEADER, ["Content-Type: application/json"])
    f = open('./data/population_data_partition.json', 'r')
    data = f.read()
    crl.setopt(pycurl.POST, 1)
    crl.setopt(pycurl.POSTFIELDS, data)
    crl.perform()
    crl.close()
    f.close()
    # create view
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/%s/_design/population?partitioned=true'% (user, password, db_ip, auriandb))
    dat_file = open('./data/views/population.js')
    crl.setopt(crl.UPLOAD, 1)
    crl.setopt(crl.READDATA, dat_file)
    crl.perform()
    crl.close()
    dat_file.close()


if dbname in couchserver:
    db = couchserver[dbname]
else:
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/%s?partitioned=true'% (user, password, db_ip, dbname))
    crl.setopt(crl.UPLOAD, 1)
    crl.perform()
    crl.close()
    db = couchserver[dbname]
    # create view
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/%s/_design/count?partitioned=true'% (user, password, db_ip, dbname))
    dat_file = open('./data/views/count.js')
    crl.setopt(crl.UPLOAD, 1)
    crl.setopt(crl.READDATA, dat_file)
    crl.perform()
    crl.close()
    dat_file.close()


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            geo_place = status.place.full_name
            place_list = geo_place.split(", ")
            if 'New South Wales' in place_list:
                partitionId = 'nsw:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Victoria' in place_list:
                partitionId = 'vic:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Western Australia' in place_list:
                partitionId = 'wa:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Australian Capital Territory' in place_list:
                partitionId = 'act:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Queensland' in place_list:
                partitionId = 'qld:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Northern Territory' in place_list:
                partitionId = 'nt:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'South Australia' in place_list:
                partitionId = 'sa:'+ str(status._json['id'])
                db[partitionId]=status._json
            if 'Tasmania' in place_list:
                partitionId = 'tas:'+ str(status._json['id'])
                db[partitionId]=status._json
        except:
            pass

    def on_error(self, status_code):
        print("error!!")


# authentication
consumer_key = '16wcvmOZByxO3im2BMiEhJqdn'
consumer_secret = 'hcmmZ1xZLQtWswqO0djGxFj7fiasOohYaPQjZ6wt5uBg6Cwzh3'
access_token = '1106041594837262340-izIjNwapHLVyyf48j6xk0y7FxrmFwt'
access_token_secret = 'pW0alYhRQOQBsvn24Epk4L3fbCwYc8PdXnz3KRuKaeBBX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['nightclub','bar'], locations=[113.080648, -44.134922, 155.252163, -10.768672])
