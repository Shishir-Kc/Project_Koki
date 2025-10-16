from fastapi import FastAPI
import uvicorn
from Models.Chat_Bot import AI
from Pydantic_Model import Prompt
from Agents.agent import Agent
from fastapi.middleware.cors import CORSMiddleware



ai = Agent()

class Server():

    def __init__(self):
        self.app  = FastAPI()
        self.set_up_routes()


    def set_up_routes(self):
        @self.app.get("/")
        def home():
            return {
                "message":"hello  !"
            }    
        @self.app.post("/chat/")
        async def get_response(data:Prompt):
            response = await ai.send_message(prompt=data.prompt)
            print(response)
            return {
                'response':response
            }

#     def run(self):
#         uvicorn.run(self.app, host="127.0.0.1", port=8000)

# if __name__ == "__main__":
#     server = Server()
#     server.run()

server = Server()
app = server.app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)