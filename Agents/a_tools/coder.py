from groq import Groq
from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY ")

def code(prompt:str)->str:
   """
    use this function when ever you are given task to generate code !
    ARGS:
    prompt:str - > describe what type of code you wnat to generate and in which language ! 
 
 
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
   print("=========================================")
   print("activated coder !")
   return data
    


if __name__ == "__main__":
    print(code(prompt=input(":>")))