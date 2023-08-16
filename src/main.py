from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import pandas as pd

from model import load_model, load_encoder
from models.person import Person
from examples.person import PersonExample

models = {}

app = FastAPI()

bearer = HTTPBearer()

def get_username_from_token(token):
  if token == "abc123":
    return "guishow"
  
  return ""

async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
  token = credentials.credentials

  username = get_username_from_token(token)
  if username == "":
    raise HTTPException(status_code = 401, detail = "Invalid token")
  
  return {"username": username}

@app.on_event("startup")
async def startup_event():
  models["model"] = load_model()
  models["ohe"] = load_encoder()

@app.get("/")
async def root():
  return "Model API is alive!"

@app.post("/predict")
async def predict(person: PersonExample, user=Depends(validate_token)):
  """
  Route to make predictions!
  """
  
  # Load the models
  ohe = models["ohe"]
  model = models["model"]

  df_person = pd.DataFrame([person.model_dump()])

  person_t = ohe.transform(df_person)
  prediction = model.predict(person_t)[0]

  return {"prediction": str(prediction), "username": user["username"]}