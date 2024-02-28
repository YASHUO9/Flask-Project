from flask import Flask,request,render_template,jsonify
import json


app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to the Flask World!"

@app.route('/home')
def home():
    return "This is the home page"


@app.route('/calculator',methods=['GET'])
def calculator():
    num1 = request.json['num1']
    num2 = request.json['num2']
    operation = request.json['operation']
    
    if operation == 'add':
        result = int(num1) + int(num2)
        
    elif operation == 'subtract':
        result = int(num1) - int(num2)
    
    elif operation == 'multiply':
        result = int(num1) * int(num2)
     
    elif operation == 'divide':
        result = int(num1) / int(num2)
    
    else:
        result = "Invalid Operation"
        
    return "the operation {} and the result is {}".format(operation,result)






if __name__ == '__main__':
    app.run(debug=True)