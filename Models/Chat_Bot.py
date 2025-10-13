from groq import Groq
from dotenv import load_dotenv
import os 
load_dotenv()


class AI():
    def __init__(self,api_key=os.environ.get("GROK_API_KEY"),prompt="Hello !",model="openai/gpt-oss-120b"):
        self.api_key = api_key
        self.prompt =  prompt
        self.model = model

        if "groq" in model:

         self.client = client = Groq(
           default_headers={
           "Groq-Model-Version": "latest"
           },
         api_key=os.environ.get("GROK_API_KEY")
         )
        else:
           self.client = client = Groq(
         api_key=os.environ.get("GROK_API_KEY")
         )

    async def response(self):
        completion = self.client.chat.completions.create(
        model="groq/compound",
        messages=[
        {
         "role": "user",
         "content": self.prompt
       }
     ],
     temperature=1,
     max_completion_tokens=1024,
     top_p=1,
     stream=True,
     stop=None)
        data = ""
        for chunnk in completion:
           if chunnk.choices[0].delta.content:
               data += chunnk.choices[0].delta.content
        return data



if __name__ == "__main__":
   while True:
    ai = AI(prompt=input(":>"))
    print(ai.response())