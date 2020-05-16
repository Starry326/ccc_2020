from flask import Flask, request, Response, render_template, make_response
from flask_restful import Api, Resource, reqparse, abort
from dataProcess import gainTweetsData, gainAurinData, gainProportion
import os.path

def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    return (app)

app = create_app()
api = Api(app)

keywords = ["nightclub", "bar"]

class Scenario1(Resource):
    def get(self):
        regions = ["nsw", "qld", "sa", "tas", "vic", "wa", "act", "nt"]
        #regions = ["nsw"]
        tweets = dict()
        tweets["total"] = 0
        tweets["distribution"] = []
        for region in regions:
            count = gainTweetsData(region)
            tweets["total"] += count
            tweets["distribution"].append({"region": region, "count": count})
        return make_response(render_template('scenario1.html', keywords=keywords, regions=regions, tweets=tweets))

api.add_resource(Scenario1, '/starry_app/gain_data')

class gainData(Resource):
    def get(self, region):
        tweetData = gainTweetsData(region)
        aurinData = gainAurinData(region)
        proportion = gainProportion(aurinData)
        results = dict()
        results['population_data'] = proportion
        results['tweets_count'] = tweetData
        return make_response(render_template('scenario1Region.html', keywords=keywords, results=results, region=region.upper()))

api.add_resource(gainData, '/starry_app/gain_data/<region>')

class Index(Resource):
    def get(self):
        return make_response(render_template('index.html', current_ip='starry'))

api.add_resource(Index, '/index')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
