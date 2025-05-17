from openai import OpenAI
client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

message = input("Cual es tu pregunta? ")

prompt = (
    "por favor responde de manera clara y sin simbolos innesesarios"
    "Evita usar idiomas que no sean el español y escribe una respuesta concisa"
    f"pregunta del usuario: {message}"
)

completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages = [
        {
          "role": "user", 
          "content": prompt
        }
    ],
)
print(completion.choices[0].message.content)