from openai import OpenAI
from fastapi import APIRouter
from interfases.chatinterfases import InputMessage


router = APIRouter()
client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")
@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message"+data["message"])

    message = "por favor responde de manera clara y sin simbolos innesesarios" 
    
    try:
        completion = ChatCompletionResponse = client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
               {
                "role": "system",
                "content":"Eres un asistente de IA que responde preguntas en español, por favor responde de manera clara y sin simbolos innesesarios"
                },
                {
                  "role": "user",
                  "content": message+"responde la pregunta:"+data["message"]
                }
             ]
        )
        print("responde"+completion.choices[0].message.content)
        return {"response":completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: " + str(e))
        return {"response":"Error", "message": str(e)}
    

@router.post("/ai-chat2")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message"+data["message"])

    message = "por favor responde de manera clara y sin simbolos innesesarios" 
    
    try:
        completion = ChatCompletionResponse = client.chat.completions.create(
            model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
            messages=[
               {
                "role": "system",
                "content":"Eres un asistente de IA que responde preguntas en español, por favor responde de manera clara y sin simbolos innesesarios"
                },
                {
                  "role": "user",
                  "content": message+"responde la pregunta:"+data["message"]
                }
             ]
        )
        print("responde"+completion.choices[0].message.content)
        return {"response":completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: " + str(e))
        return {"response":"Error", "message": str(e)}
   
