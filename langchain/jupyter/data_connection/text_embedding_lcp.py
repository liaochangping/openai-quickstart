#针对transform后的数据，进行embedding操作，embedding是将高维向量转化为低维向量，这样可以减少计算量，同时保留原有的语意信息。
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

####1. 读取文本内容
with open('./langchain/tests/state_of_the_union.txt') as f:
    text_union = f.read()


####2. 开始对文本进行分割
character_text_splitter = RecursiveCharacterTextSplitter(chunk_size= 100,
                                                         chunk_overlap= 20,
                                                         length_function= len,
                                                         add_start_index = True)

#####create_documents中str是一个[List]
text_list = character_text_splitter.create_documents([text_union])
# print(type(text_list))
# print(text_list[0])
# print(text_list[1])

#生成文本字符串数组
txt_list = [ txt.page_content for txt in text_list]


embedding = OpenAIEmbeddings(openai_api_key="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")
embedding_list = embedding.embed_documents(txt_list)
print(len(embedding_list))

#查询embedding 
query_embedding = embedding.embed_query("I love you")