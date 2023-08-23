#通过Transform Chain实现快捷处理超长文本(旨在将函数上链)
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import TransformChain,LLMChain,SimpleSequentialChain

##1. 构建长文本
with open("./langchain/jupyter/chains/the_old_man_and_the_sea.txt") as f:
    novel_text = f.read()

# print(novel_text)

##2. 构建Transform Chain
def transform_func(inputs:dict)->dict:
    text = inputs["text"]
    shortened_text = "\n\n".join(text.split("\n\n")[:3]) 
    return {"output_text":shortened_text}
    
transform_chain = TransformChain(input_variables=["text"], output_variables=["output_text"], transform=transform_func)

##3. 构建llm
prompt_template = PromptTemplate.from_template("""
请总结概括下以下内容:
{output_text}                                         
""") 

llm = OpenAI(temperature=.1, max_tokens=4096, openai_api_key="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")
llm_chain = LLMChain(llm =llm, prompt=prompt_template, verbose=True)

##4. 构建Sequential Chain
sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain], verbose=True)

sequential_chain(novel_text[:100])