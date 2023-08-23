#内存用来存储chain的状态的
from langchain.chains import ConversationChain, LLMChain 
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationSummaryBufferMemory 
from langchain.llms import OpenAI

##ConversationChain 通过接收llm（没有会话能力的），通过ConversationBufferMemory对象来实现保存会话记录的能力
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=.1, openai_api_key="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")
# llm_chain = ConversationChain(llm = llm, memory= ConversationBufferMemory(), verbose=True)
# llm_chain("hi, there")
# llm_chain("nice to meet you")
# llm_chain("and you")

#当碰到历史记录过大，此时我们可使用滑动窗口来实现控制tokens数量ConversationBufferWindowMemory
llm_window_chain = ConversationChain(llm =llm, memory= ConversationBufferWindowMemory(k=1), verbose=True)
# llm_window_chain("hi, there")
# llm_window_chain("nice to meet you")
# llm_window_chain("and you")

#ConversationSummaryBufferMemory，在内存中保留最近的交互缓冲区，但不仅仅是完全清除旧的交互，而是将它们编译成摘要并同时使用。
llm_window_chain = ConversationChain(llm =llm, memory= ConversationSummaryBufferMemory(max_token_limit=10), verbose=True)
llm_window_chain("hi, there")
llm_window_chain("nice to meet you")
llm_window_chain("and you")