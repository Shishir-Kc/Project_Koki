from fastapi import FastAPI
import uvicorn
from Models.Chat_Bot import AI
from Pydantic_Model import Prompt


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
            response = await AI(prompt=data.prompt).response()
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