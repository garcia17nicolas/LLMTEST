from openai import OpenAI
from fastapi import APIRouter
from interfases.chatinterfases import InputMessage


router = APIRouter()
client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")
@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message" + data["message"])

    message = "por favor responde de manera clara y sin simbolos innesesarios" 
    
    try:
        completion = ChatCompletionResponse = client.chat.completions.create(
            model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
            messages=[
               {
                "role": "sistem",
                "content":"Eres un asistente de IA que responde preguntas en español, por favor responde de manera clara y sin simbolos innesesarios" \
                },
                {
                  "role": "user",
                  "content": message+ "responde la pregunta:" + data["message"]
                }
             ]
        )
        print("responde"+ completion.choices[0].message.content)
        return {"status":"OK", "data": completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: " + str(e))
        return {"status":"Error", "message": str(e)}
