import pycurl
import json
from io import BytesIO 

user = "admin"
password = "admin"
db_ip = '127.0.0.1'

def gainTweetsData(region):
    b_obj = BytesIO() 
    crl = pycurl.Curl() 
    # Set URL value
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/starry_data/_partition/%s/_design/count/_view/tweets-count?reduce=true&group_level=0'% (user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform() 
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region) 
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    return(result)

def gainAurinData(region):
    result_list = dict()
    for age in range(0,86,5):
        b_obj = BytesIO() 
        crl = pycurl.Curl() 
        # Set URL value
        if(age != 85):
            crl.setopt(crl.URL, 'http://%s:%s@%s:5984/population/_partition/%s/_design/population/_view/%s-%s-count?reduce=true&group_level=0'% (user, password, db_ip, region, str(age), str(age+4)))
        else:
            crl.setopt(crl.URL, 'http://%s:%s@%s:5984/population/_partition/%s/_design/population/_view/over85-count?reduce=true&group_level=0'% (user, password, db_ip, region))
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.perform() 
        crl.close()
        get_body = b_obj.getvalue()
        # get the result(count of tweets in this region) 
        result = json.loads(get_body.decode('utf8'))
        result = result['rows'][0]['value']
        if(age != 85):
            key = str(age)+'-'+str(age+4)
        else:
            key = 'over85'
        result_list[key]=result
    return(result_list)

def gainProportion(populationList):
    total_population = 0
    proportion = dict()
    for v in populationList.values():
        total_population += v
    for k,v in zip(populationList.keys(), populationList.values()):
        proportion[k] = v/total_population
    proportion['total_population'] = total_population
    return(proportion)