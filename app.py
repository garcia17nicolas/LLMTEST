from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

from interfases.chatinterfases import InputMessage

app = FastAPI()


client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

@app.get("/")
def index():
    return {"message": "API is running"}

@app.post("/ai-chat")
def aiChat(data:InputMessage):  
    data = data.model_dump()
    print("message" + data["message"])
    return {"status": "OK"}
