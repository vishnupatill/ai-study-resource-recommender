from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add ML folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ml"))

from recommender import recommend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    topic: str


@app.post("/recommend")
def get_recommendations(query: Query):
    results = recommend(query.topic)
    return {"recommendations": results.to_dict(orient="records")}