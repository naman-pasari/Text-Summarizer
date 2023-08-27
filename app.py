from fastapi import FastAPI
import uvicorn
from src.TextSummarizer.exception import *
import os
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.TextSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    



@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)