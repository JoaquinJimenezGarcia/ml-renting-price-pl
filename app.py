from flask import Flask, render_template, make_response
from flask import request
import os
import time
import joblib
import sklearn

app = Flask(__name__)

def index():
    square_meters = request.args.get('square_meters')
    rooms = request.args.get('rooms')
    center_distance = request.args.get('center_distance')

    print(square_meters)

    if square_meters == None or rooms == None or center_distance == None:
        context = { 'model_answer': "Please, insert values to get a prediction" }
    else:
        model = joblib.load('./model.joblib')
        predict = model.predict([[square_meters, rooms, center_distance]])
        print(predict)

        context = { 'model_answer': "Renting price based on the data: " + str(predict[0]) + "PLN" }

    return render_template('index.html', context=context)

app.add_url_rule('/', '/', index) 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))