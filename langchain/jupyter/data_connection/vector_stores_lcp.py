#将embedding的数据存储到向量数据库中，用于后续的操作
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma  

####1. 读取文本内容
raw_documents = TextLoader("./langchain/tests/state_of_the_union.txt").load()
    
####2. 开始对文本进行分割
text_splitter = CharacterTextSplitter(chunk_size= 100, chunk_overlap= 0)
text_splitter_list = text_splitter.split_documents(raw_documents)
# print(text_splitter_list[0].page_content)

####3. 开始对文本进行embedding
embedding = OpenAIEmbeddings(openai_api_key="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")

# ####4. 开始入向量数据库
# db = Chroma.from_documents(text_splitter_list, embedding, persist_directory="./chroma_db")

db3 = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

#####5. 开始查询（文本查询）
# query_docs = db.similarity_search("who is the current president")
# print([doc.page_content for doc in query_docs])

#####6. 开始查询（嵌入向量）
query_embedding = embedding.embed_query("who is the current president")
query_new_docs = db3.similarity_search_by_vector(query_embedding)
print([doc.page_content for doc in query_new_docs])

