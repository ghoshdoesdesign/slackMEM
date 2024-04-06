from langchain_community.document_loaders import TextLoader

import os
os.environ['OPENAI_API_KEY'] = "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"

loader = TextLoader("/Users/samriddhoghosh/Desktop/Early/doc.txt")
documents = loader.load()

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)

retriever = db.as_retriever()

from langchain.tools.retriever import create_retriever_tool

tool = create_retriever_tool(
    retriever,
    "search_the_text",
    "Reads and retrieves actionable items or todos from slack messages.",
)
tools = [tool]

from langchain import hub

prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.messages

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

from langchain.agents import AgentExecutor, create_openai_tools_agent

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# result = agent_executor.invoke({"input": "hi, im bob"})

# result["output"]

user_input = input("Please enter some text: ")

result = agent_executor.invoke(
    {
        "input": user_input
    }
)
print(result)
result["output"]
