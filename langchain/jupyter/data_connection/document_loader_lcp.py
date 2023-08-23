#学习使用loader来加载不同数据源的数据，并统一转化为document数组对象
#1. 使用TextLoader加载text文本
# from langchain.document_loaders import TextLoader

# text_loader = TextLoader("./langchain/tests/state_of_the_union.txt")
# text_content = text_loader.load()
# print(f"count:{text_content.count}")
# print(text_content[0].page_content) #打印第一条数据
# print(type(text_content[0])) #<class 'langchain.schema.document.Document'>
# print(type(text_content[0].page_content))
# print(text_content[0].page_content[:100]) #打印第一条数据的前100个字符

#2. pdf文档加载器
from langchain.document_loaders import PDFMinerLoader

##使用的绝对路径
pdf_loader = PDFMinerLoader("./langchain/tests/pdf_loader.pdf")
pdf_data = pdf_loader.load()
print(pdf_data[0].page_content)

