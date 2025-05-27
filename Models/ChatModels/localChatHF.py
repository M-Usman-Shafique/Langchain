## Run: python3 Models/ChatModels/localChatHF.py
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llmHF = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens=50
    )
)

model = ChatHuggingFace(llm=llmHF)
result = model.invoke("What's the capital of France?")

print(result.content)