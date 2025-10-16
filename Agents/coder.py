from groq import Groq
from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY ")

def code(prompt:str)->str:
   """
   
 
 
 """

   client = Groq(api_key=api_key)
   completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[
      {
        "role": "user",
        "content": prompt
      },
      {
        "role": "system",
        "content": ""
      },
    ],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=0.95,
    reasoning_effort="default",
    stream=True,
    stop=None
)
   data = ""
   for chunnk in completion:
      if chunnk.choices[0].delta.content:
        data += chunnk.choices[0].delta.content
   return data
    


if __name__ == "__main__":
    print(code(prompt=input(":>")))