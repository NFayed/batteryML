from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('hello.html')

#from flask import Flask, request, jsonify
#from battery import predict_value

#app = Flask(__name__)

#@app.route('/predict', methods=['POST'])
#def predict():
#    data = request.json  # Get the input data from the request's JSON body
#   result = predict_value(data)  # Call the predict_value function with the input data
#  return jsonify({'prediction': result})  # Return the prediction as a JSON response

#if __name__ == '__main__':
#   app.run()