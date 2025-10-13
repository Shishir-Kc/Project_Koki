import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ.get("HF_TOKEN"),
)



completion = client.chat.completions.create(
    model="openai/gpt-oss-120b:fireworks-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the weather like in Paris today?"
        }
    
    ],
)




reasoning = completion.choices[0].message.content
print("Content:\n", reasoning)


