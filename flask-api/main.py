from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import ourModel

app = Flask(__name__)

api = Api(app)


class price_predict(Resource):

    def post(self):

        data = request.get_json()
        return jsonify(ourModel.price_predict(data["Item"], data["State"], data["Weekend"], data["Grade"], data["Organic"], data["RPS"], data["DFD"], data["Freshness"], data["Seasonal"], data["Otipy_Certified"], data["Unique_Customers"], data["demand"]))


api.add_resource(price_predict, '/price_predict')

if __name__ == '__main__':
    app.run()
