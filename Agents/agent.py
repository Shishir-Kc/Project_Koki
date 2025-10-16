from dotenv import load_dotenv
import os 
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage
import asyncio
from .image_process import image_content
from .coder import code
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph

load_dotenv()



class Agent:
   def __init__(self):
      self.checkpointer = InMemorySaver()
      self.api_key = os.environ.get("GROQ_API_KEY")
      if not self.api_key:
         raise ValueError("GROQ_API_KEY not found in environment variables")
      self.model = init_chat_model("openai/gpt-oss-120b", model_provider="groq")
      self.tools=[self.get_weather,self.time,self.lights_control,self.play_music,image_content,code]
    
      self.agent = create_react_agent(model=self.model,
                           tools=self.tools,
                        
                           prompt="",
                           checkpointer=self.checkpointer
                           )
      
            


   def get_weather(self,location:str)->str:
     """
         get weather info from live servers !
     
     """
     return f"current weather of {location} is sunny"

   def time(self,location:str)->str:
    """
    
        gets time of particular location
    
   """
    return f"Current time in {location} is 18:15"

   def lights_control(self,status:int)->str:
    """
     turn th elights on or off 

     1: on
     0 : off
   
    """
    return f"lights are {status}"

   def play_music(self,music_name:str)->str:
     """
         Plays the music from spotify ! 
         usually for party and chill phase   !
    """

     return f"playing {music_name} . . . . . ."




   
   async def send_message(self,prompt,thread_id:str="1"):
        msg = prompt
        response= self.agent.invoke(
          {'messages':[{"role":"user","content":msg}]},
          {'configurable':{"thread_id":thread_id}}                          )
        final_ai_message = None
        for m in reversed(response["messages"]):
         if isinstance(m, AIMessage) and m.content:
          final_ai_message = m
          break

        print("=========================================================")
        if "reasoning_content" in final_ai_message.additional_kwargs:
         print(f"REASONING -> {final_ai_message.additional_kwargs['reasoning_content']}")
         print(f"RESPONSE -> {final_ai_message.content}")
        try: 
         reasoning_content =final_ai_message.additional_kwargs['reasoning_content']
         response_got = final_ai_message.content
        except KeyError:
          reasoning_content = " "
          response_got = final_ai_message.content
        return {
          'reasoning':reasoning_content,
          'response':response_got
        }

if __name__=="__main__":
  ai = Agent()
  asyncio.run(ai.send_message(prompt=input()))
