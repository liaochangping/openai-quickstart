#self_ask_with_search 作为agent类型的一种，它仅仅支持一个tool
from langchain import OpenAI, SerpAPIWrapper 
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=.1, openai_api_key="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")
search = SerpAPIWrapper(serpapi_api_key="adbef525f8bd317d7ef7783212fe89ae316da4fe40450b3162f8d7c4e4e37839")
tools = [
    Tool(name="Intermediate Answer", func=search.run, description="useful for when you need to ask with search")
]
self_ask_agent = initialize_agent(llm=llm,
                                  agent=AgentType.SELF_ASK_WITH_SEARCH, 
                                  tools=tools, verbose=True)

print(self_ask_agent("how old is the current president of the united states?"))
