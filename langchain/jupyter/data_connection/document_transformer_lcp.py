#data connection中数据转化的处理，transform
##原理：先按照分隔符\\n\\n,\\n，一般存在这样的分隔符，说明两段之间不再相同语意。然后再按照''分割，然后根据最大trunk的大小来组合字符，从而形成trunk块，用于embedding操作。这样可以保证每个trunk块的语意是一致的。
##1. CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

####1. 读取文本内容
with open('./langchain/tests/state_of_the_union.txt') as f:
    text_union = f.read()

print(text_union[:100])


####2. 开始对文本进行分割
character_text_splitter = RecursiveCharacterTextSplitter(chunk_size= 100,
                                                         chunk_overlap= 20,
                                                         length_function= len,
                                                         add_start_index = True)

#####create_documents中str是一个[List]
text_list = character_text_splitter.create_documents([text_union])
# print(type(text_list))
print(text_list[0])
print(text_list[1])

#####2.1 添加metadata
text_meta_list = character_text_splitter.create_documents([text_union],[{"document":1}, {"document":2}])
print(text_meta_list[0])
print(text_meta_list[1])


####2. 读取html内容
html_text = """
<!DOCTYPE html>
<html>
    <head>
        <title>🦜️🔗 LangChain</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                color: darkblue;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>🦜️🔗 LangChain</h1>
            <p>⚡ Building applications with LLMs through composability ⚡</p>
        </div>
        <div>
            As an open source project in a rapidly developing field, we are extremely open to contributions.
        </div>
    </body>
</html>
"""

html_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.HTML,
                                                             chunk_size= 60,
                                                         chunk_overlap= 0,
                                                         add_start_index = True)
html_splitter_list = html_splitter.create_documents([html_text])
print(len(html_splitter_list))

for txt in html_splitter_list :
    print(txt)
