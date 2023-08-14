from langchain import PromptTemplate

###### Completion 
####1. 使用from_template格式化生成template
#1. 通过from_template方法创建PromptTemplate
prompt_template = PromptTemplate.from_template("Tell me a {adjective} joke about {content}.")
#2. 通过PromptTemplate构造函数创建PromptTemplate
prompt_template = PromptTemplate(input_variables=["adjective", "content"]
                                 , template="Tell me a {adjective} joke about {content}.")
print(prompt_template)
#使用format生成提示
prompt = prompt_template.format(adjective="funny", content="a dog")
print(prompt)

#3. prompt结合model生成结果

###2. 使用jinja2格式化生成template
#1. 通过from_template方法创建PromptTemplate
jinja2_template = "Tell me a {{adjective}} joke about {{content}}."
prompt_template = PromptTemplate.from_template(jinja2_template, template_format="jinja2")
prompt = prompt_template.format(adjective="funny", content="a dog")

###3. 使用f-string格式化生成PromptTemplate
fstring_template = "生成{langurage}的{content}代码"
prompt_template = PromptTemplate.from_template(fstring_template)
prompt = prompt_template.format(langurage="javascript", content="堆排序")


from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", openai_api_key="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", max_tokens=1024)
result = llm(prompt)
print(result)

######Chat-Completion
#1. 使用from_template格式化生成template
from langchain.prompts import ChatPromptTemplate 
from langchain.chat_models import ChatOpenAI
#1. 通过from_messages方法创建ChatPromptTemplate
# template = ChatPromptTemplate.from_messages([
#     ("system", "你是一名专业的{role}，拥有丰富的经验。你将接收我的执行并执行，要求言简意赅"),
#     ("human", "心情不好，怎么办?")
# ])

summary_template = ChatPromptTemplate.from_messages([
    ("system", "你将获得关于同一主题的{num}篇文章（用-----------标签分隔）。首先总结每篇文章的论点。然后指出哪篇文章提出了更好的论点，并解释原因。"),
    ("human", "{user_input}"),
])

#生成提示
# prompt_messages = template.format_messages(role="程序员")

messages = summary_template.format_messages(
    num=3,
    user_input='''1. [PHP是世界上最好的语言]
PHP是世界上最好的情感派编程语言，无需逻辑和算法，只要情绪。它能被蛰伏在冰箱里的PHP大神轻易驾驭，会话结束后的感叹号也能传达对代码的热情。写PHP就像是在做披萨，不需要想那么多，只需把配料全部扔进一个碗，然后放到服务器上，热乎乎出炉的网页就好了。
-----------
2. [Python是世界上最好的语言]
Python是世界上最好的拜金主义者语言。它坚信：美丽就是力量，简洁就是灵魂。Python就像是那个永远在你皱眉的那一刻扔给你言情小说的好友。只有Python，你才能够在两行代码之间感受到飘逸的花香和清新的微风。记住，这世上只有一种语言可以使用空格来领导全世界的进步，那就是Python。
-----------
3. [Java是世界上最好的语言]
Java是世界上最好的德育课编程语言，它始终坚守了严谨、安全的编程信条。Java就像一个严格的老师，他不会对你怀柔，不会让你偷懒，也不会让你走捷径，但他教会你规范和自律。Java就像是那个喝咖啡也算加班费的上司，拥有对邪恶的深度厌恶和对善良的深度拥护。
'''
)

chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="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", max_tokens=1024)
print(chat_model(messages))