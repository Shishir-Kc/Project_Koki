# import requests
# import random
# import httpx
# import asyncio


# async def api_call(times =10 ):
#     called = 0
#     url = "http://127.0.0.1:8000/chat/"
#     prompts = [
#         'Hello !',
#         "write an essay on ai in 200 words",
#         'explain life in brief',
#         "hahaha ",
#         "hello world",
#         "py code to print 100 num ",
#     ]

#     payload = { 
#         'prompt': random.choice(prompts)
#     }
#     while called < int(times):
#         print("===========================PAYLOAD=========================")
#         print(payload)
#         async with httpx.AsyncClient(timeout=700) as client:  
           
#          response = await client.post(url,json=payload)
#          print("===========================RESPONSE=======================")
#          print(response.json())
#         called +=1

# if __name__ == "__main__":
#  asyncio.run(api_call(times=input(">")))




import asyncio
import random
import httpx

async def send_single_request(url, prompt):
    payload = {'prompt': prompt}
    print(f"Sending: {payload}")
    
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            asyncio.sleep(0.5)
            response = await client.post(url, json=payload)
            print(f"Response: {response.json()}")
        except httpx.RequestError as e:
            print(f"Request failed: {e}")

async def api_call(times=10):
    url = "http://127.0.0.1:8000/chat/"
    prompts = [
        'Hello !',
        "write an essay on ai in 200 words",
        'explain life in brief',
        "hahaha ",
        "hello world",
        "py code to print 100 num ",
    ]

    tasks = []

    for _ in range(times):
        prompt = random.choice(prompts)
        tasks.append(send_single_request(url, prompt))

   
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    times = input("Number of concurrent requests to send: ")
    asyncio.run(api_call(times=int(times)))
