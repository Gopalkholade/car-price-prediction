from fastapi import FastAPI
import pickle
import json
import uvicorn
from modelInputs import ModelInputs
import pandas as pd
import numpy as np

model=pickle.load(open("./models/modelPipe.pkl","rb"))


app = FastAPI(debug=True)

@app.post('/predict')
def predictor(input_parameters:ModelInputs):
    input_parameters=input_parameters.json()
    input_parameters=json.loads(input_parameters)

    data=pd.DataFrame(np.array(list(input_parameters.values())).reshape(1,-1),columns=input_parameters.keys())
    pred = model.predict(data)
    return {"Prediction":pred}
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)