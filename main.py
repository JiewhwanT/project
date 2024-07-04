# model
from model_lstm import predict_lstm as model_predict_lstm
from model_cnn import predict_cnn as model_predict_cnn
from model_bert import predict_bert as model_predict_bert
from model_xlm_r import predict_xlm_r as model_predict_xlm_r 

# Web Server
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from pydantic import BaseModel
from typing import List


# create app
app = FastAPI()
# alow cross origin all origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# index route
@app.get('/')
def index():
    return {'message': 'This is a sentiment analysis model API.'}

#lstm
@app.get('/predict_lstm')
def predict(text: str):
    return {
        'inputText': text, 
        'sentiment': model_predict_lstm(text, decode=True)
    }

#cnn
@app.get('/predict_cnn')
def predict(text: str):
    return {
        'inputText': text, 
        'sentiment': model_predict_cnn(text, decode=True)
    }


# PhayaThai
@app.get('/predict_bert')
def predict(text: str):
    return {
        'inputText': text,
        'sentiment': model_predict_bert(text, decode=True)
    }


# XLM-R
@app.get('/predict_xlm_r')
def predict(text: str):
    return {
        'inputText': text,
        'sentiment': model_predict_xlm_r(text, decode=True)
    }



# start server
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)