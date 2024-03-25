import joblib
import xgboost
import numpy as np

from flask import Flask, request, jsonify

app = Flask(__name__)

#Loading the model at startup
@app.route("/")
def startup():
    AI_model = joblib.load('XGB_model.joblib')
    return "AI model has been loaded"

#POST method for giving the data for prediction
#The web app should give a json dictionary in the format of: {"H_Init": number, "R_Intensity": number}
#Example formatting of dictionary: {"H_Init" : 1.057 , "R_intensity" : 76}

@app.route("/predict", methods=['POST'])
def getdata():

    #importing the AI model

    AI_model = joblib.load('XGB_model.joblib')

    #Turning the given dictionary's values (data_for_prediction) to a numpy array (data_array)

    data_for_prediction = request.get_json()
    data_array = np.array(list(data_for_prediction.values()))
    
    #Predicting the Flood height based on the given Initial Height (H_Init) and Rain Intensity (R_Intensity)
    prediction = AI_model.predict([data_array])

    prediction = float(prediction)

    #Returning the predicted number
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug = True)