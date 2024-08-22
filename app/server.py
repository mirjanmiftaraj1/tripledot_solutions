from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel
from typing import List

# Load the model

import os 
os.getcwd()
#model_path = r'C:\Users\kuksj\Downloads\TrippleDotTask\app\random_forest_classifier_model.joblib'
model_path = r'random_forest_classifier_model.joblib'
model = joblib.load(model_path)

class_names = np.array(['Low', 'Medium', 'High'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Housing model API is OK'}

class Features(BaseModel):
    features: List[float]

@app.post('/predict')
def predict(data: Features):
    """
    Predicts the class of a given set of features.

    Args:
        data (Features): A pydantic model containing the features to predict.

    Returns:
        dict: A dictionary containing the predicted class.
    """
    features = np.array(data.features).reshape(1, -1)
    
    # Check if the features are of the correct shape
    if features.shape[1] != model.n_features_in_:
        raise HTTPException(status_code=400, detail=f"Expected {model.n_features_in_} features, got {features.shape[1]}.")

    try:
        prediction = model.predict(features)
        class_name = class_names[prediction[0]]
        #class_name = prediction[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {'predicted_class': class_name}