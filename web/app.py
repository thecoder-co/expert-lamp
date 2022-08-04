from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if 'x' not in posted_data or 'y' not in posted_data:
        return 301
    else:
        return 200


class Add(Resource):
    def post(self):
        # If I'm here, POST was called
        # step 1 get posted datacd web

        posted_data = request.get_json()

        # check posted data

        status_code = check_posted_data(posted_data, "add")

        if status_code != 200:
            return {'status_code': status_code, 'message': 'You left out a param'}, status_code

        x = posted_data['x']
        y = posted_data['y']

        x = int(x)
        y = int(y)

        ret = x + y
        retMap = {
            'message': ret,
            'status_code': 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        # If I'm here, POST was called
        # step 1 get posted data
        posted_data = request.get_json()

        # check posted data

        status_code = check_posted_data(posted_data, "subtract")

        if status_code != 200:
            return {'status_code': status_code, 'message': 'You left out a param'}, status_code

        x = posted_data['x']
        y = posted_data['y']

        x = int(x)
        y = int(y)

        ret = x - y
        retMap = {
            'message': ret,
            'status_code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    pass


class Divide(Resource):
    pass


api.add_resource(Add, '/add')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hithere')
def hithere():
    return 'I just hit /hithere'


@app.route('/bye')
def bye():
    # c = 1/0
    return jsonify({'message': 'Bye!'})


@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict['x']
    y = dataDict['y']
    return jsonify({'sum': x + y}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
