from flask import Flask, request, Response, render_template, make_response
from flask_restful import Api, Resource, reqparse, abort
from dataProcess import gainTweetsData, gainAurinData, gainProportion, gainTweetsData2, gainAurinData2, gainAurinData3, gainTweetsData3, gainAurinData4
import os.path

keywords = {"scenario1": ["nightclub", "bar"],
            "scenario2": ["covid-19", "coronavirus"],
            "scenario3": []}
regions = ["nsw", "qld", "sa", "tas", "vic", "wa", "act", "nt"]

def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    return (app)

app = create_app()
api = Api(app)

class Scenario1(Resource):
    def get(self):
        results = dict()
        for region in regions:
            tweet_data = gainTweetsData(region)
            aurin_data = gainAurinData(region)
            proportion = gainProportion(aurin_data)
            result = dict()
            result['population_data'] = proportion
            result['tweets_count'] = tweet_data
            results[region] = result
        return make_response(render_template('scenario1.html', keywords=keywords['scenario1'], regions=regions, results=results))

api.add_resource(Scenario1, '/starry_app/gain_data')

class Scenario2(Resource):
    def get(self):
        results = dict()
        for region in regions:
            tweet_data = gainTweetsData2(region)
            hospital_data = gainAurinData2(region)
            income_data = gainAurinData3(region)
            result = dict()
            result['hospital_count'] = hospital_data
            result['income'] = income_data
            result['tweets_count'] = tweet_data
            results[region] = result
        return make_response(render_template('scenario2.html', keywords=keywords['scenario2'], regions=regions, results=results))

api.add_resource(Scenario2, '/charlie_app/gain_data')

class gainData(Resource):
    def get(self, region):
        tweetData = gainTweetsData(region)
        aurinData = gainAurinData(region)
        proportion = gainProportion(aurinData)
        results = dict()
        results['population_data'] = proportion
        results['tweets_count'] = tweetData
        return results

api.add_resource(gainData, '/starry_app/gain_data/<region>')

class gainData2(Resource):
    def get(self, region):
        tweetData = gainTweetsData2(region)
        hospitalData = gainAurinData2(region)
        incomeData = gainAurinData3(region)
        results = dict()
        results['hospital_count'] = hospitalData
        results['income'] = incomeData
        results['tweets_count'] = tweetData
        return results

api.add_resource(gainData2, '/charlie_app/gain_data/<region>')


class gainData3(Resource):
    def get(self, region):
        tweetData = gainTweetsData3(region)
        lowIncomeHouseholds = gainAurinData4(region)
        populationData = gainAurinData(region)
        results = dict()
        results['low_income_households'] = lowIncomeHouseholds
        results['population'] = populationData
        results['tweets_count'] = tweetData
        return (results)

api.add_resource(gainData3, '/travis_app/gain_data/<region>')


class Index(Resource):
    def get(self):
        return make_response(render_template('index.html', current_ip='starry'))


api.add_resource(Index, '/index')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
