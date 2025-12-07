import os
from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
import asyncio

client = MultiServerMCPClient(  
    {
        "OSDU": {
            "transport": "stdio",  # Local subprocess communication
            "command": "python",
            # Absolute path to your database_mcp_server.py file
            "args": ["database_mcp_server.py"],
        }
    }
)


async def main():
    
    tools = await client.get_tools()

    llm = AzureChatOpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                api_version="2025-01-01-preview",
                azure_deployment="gpt-4o",
                azure_endpoint=base_url,
                default_headers={"collection_name": "collectionName"},
                temperature=0,
                max_retries=3,
            )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""You are a helpful assistant that identifies the agent suitable for a given query and invokes the appropriate tool.
                                    If you don't have an appropriate tool, just respond saying 'No appropriate tools found'.""",
    )
    db_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "search for employee id 123 in Employees data collection"}]}
    )
    print (db_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

