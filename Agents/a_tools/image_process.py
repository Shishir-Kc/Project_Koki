from dotenv import load_dotenv
import os 
import requests
import json
import asyncio
import httpx
load_dotenv()
api_key = os.environ.get("IMAGE_PROCESS_API")

def image_content(url:str,prompt:str)->str:
  """
    Use this tool to get info about what are the contents present in the image !
    ARGS:
    url: -> image url 
    prompt: -> what is the information u want to get from this image ? 
  
  """
#   async with httpx.AsyncClient(timeout=9000) as client:
  response = requests.post(
   url="https://openrouter.ai/api/v1/chat/completions",
   headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",},
  data=json.dumps({
    "model": "qwen/qwen2.5-vl-32b-instruct:free",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt
          },
          {
            "type": "image_url",
            "image_url": {
              "url": url
            }
          }
        ]
      }
    ],
    
  })
)
  data = response.json()
  return (data['choices'][0]['message']['content'])

if __name__ == "__main__":
  print(asyncio.run(image_content(url=input("URL : > "),prompt=input("PROMPT : > "))))
