from flask import Flask, request, jsonify
from battery import predict_value
import numpy as np
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    #def predict(data):
    #data = request.get_json().get('data')  # Get the 'data' field from the request's JSON body
    #fixeddata = [[float(data)]]
    #result = predict_value(fixeddata)
    print('ok')
    return jsonify({'prediction': 1})
    #reshaped_data = np.array(result).reshape(-1, 1).tolist()
    # Call the predict_value function with the input data
    #return jsonify({'prediction': reshaped_data})  # Return the prediction as a JSON response

if __name__ == '__main__':
    app.run()
    #app.run(host='NFayed.pythonanywhere.com', port=5001)