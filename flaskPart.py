from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from dataProcess import gainTweetsData, gainAurinData, gainProportion

app = Flask(__name__)
api = Api(app)


class gainData(Resource):
    def get(self, region):
        tweetData = gainTweetsData(region)
        aurinData = gainAurinData(region)
        proportion = gainProportion(aurinData)
        results = dict()
        results['population_data'] = proportion
        results['tweets_count'] = tweetData
        return(results)

api.add_resource(gainData, '/starry_app/gain_data/<region>')

if __name__ == '__main__':
    app.run(debug=True)
