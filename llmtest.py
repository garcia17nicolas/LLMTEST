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