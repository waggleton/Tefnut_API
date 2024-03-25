# Tefnut_API
A flask API that contains an AI model for predicting flood.

# Setup:

1.Install required modules by typing and entering:


-pip install flask

-pip install joblib

-pip install xgboost

-pip install numpy


2.Run the server by simply running main.py by typing and entering:

-python main.py

# How does it work:


1.This API only has a POST request that should recieve a json dictionary in the format of {"H_Init": number, "R_Intensity": number}

ex. {"H_Init" : 1.057 , "R_intensity" : 76}


2.Once it recieves a dictionary it should be able to predict a data and it will return a float number in JSON form
