import httpx
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv('AI_TOKEN'),
                     http_client=httpx.AsyncClient(
                         #proxies=os.getenv('PROXY'),
                         transport=httpx.AsyncHTTPTransport(local_address="0.0.0.0"),
                     ))

async def gpt4o(question):
    response = await client.chat.completions.create(
        messages=[{"role": "user",
                  "content": str(question)}],
        model="gpt-4o"
    )
    return response