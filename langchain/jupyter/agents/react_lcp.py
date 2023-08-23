#reAct agent 作为agent类型的一种，它支持多个工具
from langchain import OpenAI, SerpAPIWrapper 
from langchain.agents import initialize_agent, load_tools
from langchain.agents import AgentType
import os 

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "adbef525f8bd317d7ef7783212fe89ae316da4fe40450b3162f8d7c4e4e37839"

llm = OpenAI(temperature=.1)

tools = load_tools(["serpapi", "llm-math"], llm=llm)
self_ask_agent = initialize_agent(llm=llm,
                                  agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                                  tools=tools, verbose=True)

print(self_ask_agent("最近一次军运会在哪里举行的？"))