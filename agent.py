from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        ## Write whatever you want
        task="Go to defillama.com and return DeFi TVL with a humanreadable timestamp",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())