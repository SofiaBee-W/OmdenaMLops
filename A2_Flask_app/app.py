from calculatebmi import calculate_bmi
from flask import Flask, app, jsonify, request

#Instantiate flask object
app =  Flask('__name__')

@app.route('/', methods = ['GET','POST'])
def get_input():
    """
    A function to get request using flask, evaluate and return result
    """
    packet = request.get_json(force=True)
    weight = packet["weight"]
    height = packet["height"]

    bmi = calculate_bmi(weight,height)

    return jsonify(packet,bmi)

# driver function to run the app

if __name__  == '__main__':
    app.run(debug = True)