from pydantic import BaseModel

class InputMessage(BaseModel):
    message: str
    model: str
class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
class Message(BaseModel):
    content: str
class Choices(BaseModel):
    message: Message
class ChatCompletionResponse(BaseModel):
    model: str
    choices: list[Choices]
    usage: Usage