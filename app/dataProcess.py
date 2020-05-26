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

def gainTweetsData2(region):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/tweets/_partition/%s/_design/count/_view/tweets-count?reduce=true&group_level=0'% (user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    return(result)

def gainAurinData2(region):
    result_list = dict()
    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/under50?reduce=true&group_level=0' % (user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "hospitals(<50 beds)"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/50-99?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "hospitals(50-99 beds)"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/100-199?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "hospitals(100-199 beds)"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/200-500?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "hospitals(200-500 beds)"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/over500?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    key = "hospitals(>500 beds)"
    if result['rows']:
        result = result['rows'][0]['value']
        result_list[key] = result
    else:
        result_list[key] = 0


    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/public?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "public hospital"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/private?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "private hospital"
    result_list[key] = result

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/hospitals/_partition/%s/_design/hospital_count/_view/total?reduce=true&group_level=0' % (
                   user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "hospital total"
    result_list[key] = result

    return(result_list)

def gainAurinData3(region):
    result_list = dict()
    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/income/_partition/%s/_design/income/_view/mean' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    for x in result['rows']:
        key = str(x['key']) + ' mean income'
        result_list[key] = x['value']

    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/income/_partition/%s/_design/income/_view/median' % (
                   user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    for x in result['rows']:
        key = str(x['key']) + ' median income'
        result_list[key] = x['value']

    return (result_list)


def gainTweetsData3(region):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL, 'http://%s:%s@%s:5984/travis_data/_partition/%s/_design/count/_view/tweets-count?reduce=true&group_level=0'% (user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    return(result)

def gainAurinData4(region):
    result_list = dict()
    b_obj = BytesIO()
    crl = pycurl.Curl()
    # Set URL value
    crl.setopt(crl.URL,
               'http://%s:%s@%s:5984/low_income_households/_partition/%s/_design/low_income_households/_view/lowIncomeHouseholds?reduce=true&group_level=0' % (
               user, password, db_ip, region))
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    # get the result(count of tweets in this region)
    result = json.loads(get_body.decode('utf8'))
    result = result['rows'][0]['value']
    key = "lowIncomeHouseholds"
    result_list[key] = result

    return (result_list)
