from flask import Flask, request, Response, render_template, make_response
from flask_restful import Api, Resource, reqparse, abort
from dataProcess import gainTweetsData, gainAurinData, gainProportion, gainTweetsData2, gainAurinData2, gainAurinData3, gainTweetsData3, gainAurinData4
import os.path




def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    return (app)


app = create_app()
api = Api(app)


class gainData(Resource):
    def get(self, region):
        tweetData = gainTweetsData(region)
        aurinData = gainAurinData(region)
        proportion = gainProportion(aurinData)
        results = dict()
        results['population_data'] = proportion
        results['tweets_count'] = tweetData
        return (results)


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
        return (results)


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