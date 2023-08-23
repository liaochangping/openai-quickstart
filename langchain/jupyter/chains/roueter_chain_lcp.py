#######有了变量，按照编程语言的习惯，就应该要有条件判断了，通过学习RouterChain，实现条件判断执行
from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.chains.router import LLMRouterChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router.llm_router import RouterOutputParser


#1. 生成不同的prompt 模版
physics_template = """
你是一名非常聪明、知识渊博的物理教授。你擅长以简洁易懂的方式回答关于物理的问题。当你不知道某个问题的答案的时候，你会坦诚承认。
这是一个问题:{input}
"""

math_template = """
你是一名非常聪明、知识渊博的数学教授。你习惯将问题分解成不同的小部分，先思考不同部分的，然后将不同部分的内容组合起来，得到最终的答案。当你不知道某个问题的答案的时候，你会坦诚承认。
这是一个问题:{input}
"""

chinese_template = """
你是一名资深的中文教授，你知识渊博，特别是对于中国古代文学和诗词有着深入的研究。你对于理解问题是从简洁、结论入手，然后再仔细分析过程部分。 当你不知道某个问题的答案的时候，你会坦诚承认。
这是一个问题:{input}
"""

prompt_infos = [
    {
        "name": "物理",
        "description":"适用于回答物理问题",
        "prompt_template": physics_template,
    },
    {
        "name": "数学",
        "description":"适用于回答数学问题",
        "prompt_template": math_template,
    },
    {
        "name": "语文",
        "description":"适用于回答语文相关的问题",
        "prompt_template": chinese_template,
    }
]

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=.8, openai_api_key="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")

#根据 prompt_infos 生成不同的prompt的llmChain
destionation_chain = {}
for info in prompt_infos :
    name = info["name"]
    prompt = info["prompt_template"]
    prompt_template = PromptTemplate.from_template(prompt)
    destionation_chain[name] = LLMChain(llm=llm, prompt=prompt_template)

#创建一个默认的train
default_chain = ConversationChain(llm=llm, output_key="text")

#使用LLMRouterChain 来决定使用哪个prompt-chain，如果没有匹配的，就使用默认的chain
##创建router的prompttemplate
destionations = [f"{p['name']}:{p['description']}" for p in prompt_infos]
destionations_str = '\n'.join(destionations)

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations = destionations_str)
router_prompt = PromptTemplate(input_variables=["input"], template=router_template, output_parser=RouterOutputParser())

#构建router_chain
router_chains = LLMRouterChain.from_llm(llm=llm, prompt=router_prompt)

#构建MultiPromptChain，其中根据路由链的推到，选择具体的目的连，如果没有选中则走默认链 
mutiply_chain = MultiPromptChain(router_chain=router_chains,
                                 destination_chains=destionation_chain,
                                 default_chain=default_chain)

print(mutiply_chain.run({"input":"你好，我想问一下，什么是牛顿第一定律？"}))
print(mutiply_chain.run({"input":"你好，我想问一下，高等数学中矩阵的定义是什么？"}))