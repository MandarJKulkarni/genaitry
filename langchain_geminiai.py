import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Set your Gemini API key as an environment variable or pass it directly
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY" # You can set it here or as an env var

# Initialize the LLM with the 'gemini-pro' model and your API key
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash") # You can also set temperature, top_p here

# Create a message to send to the LLM
message = HumanMessage(content="A joke about software development")

# Send the message and get a response
response = llm.invoke([message])

# Print the content of the response
print(response.content)
