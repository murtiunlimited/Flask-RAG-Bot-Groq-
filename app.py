from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import uvicorn 


groq_api_key = os.getenv("GROQ_API_KEY", 'gsk_xxxxx')
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", 'tvly-dev-xxxxx')

MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "groq/compound",
    "groq/compound-mini"
]

tool_tavily = TavilySearchResults(max_results=2)

tools = [tool_tavily, ]

app = FastAPI(title='LangGraph AI Agent')

class RequestState(BaseModel):
    system_prompt: str
    model_name: str
    messages: List[str]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and tools.
    Dynamically selects the model specified in the request.
    """
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)

    agent = create_agent(llm, tools=tools)

    state = {"messages": request.messages}

    result = agent.invoke(state)

    return result

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)  # Start the app on localhost with port 8000
