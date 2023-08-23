
###使用chain将多个模型串联起来，实现更复杂的功能
from langchain.llms import  OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.output_parsers import CommaSeparatedListOutputParser

###1. 使用SimpleSequentialChain 实现单一输入，单一输出的模型串联
# prompt_template = PromptTemplate.from_template("""
# 你作为名小说创造大佬，拥有丰富的小说创作经验，请以以下标题来构造一则小说简介：
# 标题:{title}
# 以下是针对标题和描述构建的简介：
# """)

# llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key="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")

# write_chain = LLMChain(llm=llm, prompt=prompt_template)
# # print(write_chain.run(title="如何战胜三体人", description="三体人是宇宙中一种具备陆海空能力的特种生命，人类由于是一种需要在特定环境下生成的生物，对于三体人这种生物，通常情况下是很难战胜的。但是，如果人类能够在三体人的生存环境中生成，那么人类就有可能战胜三体人。", verbose=True))

 
# review_prompt_template = PromptTemplate.from_template("""
# 你作为一名来自《纽约时报》的专业的评论专家，拥有大量的阅读小说经验，同时掌握对各种小说进行评论的技巧，请以以下的小说简介构造一则小说评论： 
# 简介:{synopsis}   
# 以下是来自《纽约时报》小说评论家对上述剧目的评论：                                                
# """)

# review_chain = LLMChain(llm=llm, prompt=review_prompt_template)
# print(review_chain.run({"synopsis":"《三体人不是无法战胜的》是一部关于二十一世纪新中国的历史剧。该剧讲述了一群三体人，他们来自不同的文化背景，拥有不同的思想和信仰，在新中国发展的进程中所经历的艰辛，以及他们最终克服了困难，实现和谐社会的故事。他们对新中国的发展提出了自己的见解，克服了文化"}))

# overall_chain = SimpleSequentialChain(chains=[write_chain, review_chain], input_key="title", output_key="synopsis", verbose=True)
# print(overall_chain.run("如何战胜三体人"))

###2. 使用SequentialChain 实现多输入，多输出的模型串联
llm_new = OpenAI(temperature=.7, openai_api_key="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")
mutiply_prompt_template = PromptTemplate(input_variables=["title","description"], template="""
                                                          你作为名小说创造大佬，拥有丰富的小说创作经验，请以以下标题和描述来构造一则小说简介：
标题: {title}
描述：{description}
以下是针对标题和描述构建的简介：
""")

mutiply_write_chain = LLMChain(llm=llm_new, prompt=mutiply_prompt_template, output_key="synopsis", verbose=True)

mutiply_review_template = PromptTemplate(input_variables=["synopsis"], template="""
                                         你作为一名来自《纽约时报》的专业的评论专家，拥有大量的阅读小说经验，同时掌握对各种小说进行评论的技巧，请以以下的小说简介构造一则小说评论： 
简介:{synopsis}   
以下是来自《纽约时报》小说评论家对上述剧目的评论:""")
mutiply_review_chain = LLMChain(llm=llm_new, prompt=mutiply_review_template, output_key="review", verbose=True)

sequential_chain = SequentialChain(chains=[mutiply_write_chain, mutiply_review_chain],
                                    input_variables=["title", "description"],
                                    output_variables=["synopsis", "review"],
                                    verbose=True)
a = sequential_chain({"title":"如何战胜三体人","description":"三体人是来自宇宙的新物种，他可以在任何环境下存活，它们拥有非常先进的科技能力。人类在它们面前，非常弱小。为了寻找战胜三体人的办法，中国科学家不断的研究三体人的生活习性，最终发现了战胜三体人的办法。"})
print(a)