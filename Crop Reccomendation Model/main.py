import uvicorn
from fastapi import FastAPI
from Crops import Crop
import numpy as np
import pickle
import pandas as pd


app = FastAPI()
pickle_in = open("RandomForest.pkl","rb")
classifier=pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, N'}


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}


@app.post('/predict')
def predict_crop(data:Crop):
    data = data.dict()
    # data = data.model_dump()
    N=data['N']
    P=data['P']
    K=data['K']
    temperature=data['temperature']
    humidity=data['humidity']
    ph=data['ph']
    rainfall=data['rainfall']
   
    prediction = classifier.predict([[N,P,K,temperature,humidity,ph,rainfall]])[0]
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)