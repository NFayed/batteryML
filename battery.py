import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# def train_model():
#     # importing data
#     df = pd.read_csv("battery capacity.csv", usecols=['Cycles / Days of Aging Test','Capacity [Ah]'])
#
#     X = df.drop('Capacity [Ah]', axis=1)
#     y = df['Capacity [Ah]']
#
#     # creating a regression model
#     model = LinearRegression()
#
#     # fitting the model
#     model.fit(X, y)
#
#     # Save the trained model
#     with open('model.pkl', 'wb') as file:
#         pickle.dump(model, file)
#
# def load_model():
#     # Load the trained model
#     with open('model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model

def predict_value():
    # Load the trained model
    #model = load_model()

    # Make prediction using the loaded model
    #X_test = data
    #prediction = model.predict(X_test)

    #voltage = 400
    #prediction = prediction * voltage / 1000

    #return prediction
    print('ok')

# Train the model and save it
#train_model()

# Test the predict_value function
#data = 50
#prediction = predict_value(data)
#print(prediction)
