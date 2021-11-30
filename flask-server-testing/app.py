from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Word!"

# Exemple URL : http://localhost:5000/average?integers=1&integers=5&integers=8
@app.route('/average', methods=['GET'])
def getAverage():
    integers = request.args.getlist('integers', type=int)

    if len(integers) == 0:
        return "List null"
    else:
        response = average(integers)
        return "Average is : {}".format(response)

def average(integers):
    return sum(integers)/len(integers)