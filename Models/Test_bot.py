# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()

# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.environ.get("HF_TOKEN"),
# )



# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b:fireworks-ai",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the weather like in Paris today?"
#         }
    
#     ],
# )




# reasoning = completion.choices[0].message.content
# print("Content:\n", reasoning)


from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.environ.get("OR_API_KEY")
import requests

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
while True:
    data = {
     "model": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
     "messages": [
         {"role": "system", "content": "You are a assistant "},
         {"role": "user", "content": input()}
     ]
    }

    response = requests.post(url, headers=headers, json=data)
    print('===========================================================')
    # print(response.json()["choices"][0]["message"]["content"])
    print('===========================================================')
    print(response.json())
