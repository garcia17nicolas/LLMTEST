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
    model="meta-llama/llama-3.3-8b-instruct:free",
    messages = [
        {
          "role": "user", 
          "content": prompt
        }
    ],
)
print(completion.choices[0].message.content)