
import pip
import numpy as np
import pandas as pd
import streamlit as st


from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper, SQLDatabase
#from langchain_experimental.sql import SQLDatabaseChain

import os
os.environ['OPENAI_API_KEY'] = "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"
os.environ['SERPAPI_API_KEY'] = "181c6aacc8075e235ee567884f58f298dc35033b6de749ab6537f4b7cd1655f2"
np.random.seed(0)

origin_address = st.text_input("Enter Origin Address", "Jacobs Hall, Berkeley")



# %%
import sklearn


  #if st.button("Ask Yoda"):

llm = ChatOpenAI(temperature=0, model="gpt-4-turbo-preview")
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
# db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")
# db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
    
]

system_prompt = input("Please enter your story: ")
company_input = input("Please enter the name of the company you want to generate a blurb for: ")


from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a Career advisor specializing in tech jobs - here is a profile of a candidate with their introduction: I've been a Product Designer for over three years, building SaaS products and strategies for companies such as Ripple and Amadeus. I recently completed my master's in Emerging Technology Design at UC Berkeley, focusing on leveraging design and technology to create economic opportunities for underrepresented communities. While working for Ripple, I discovered a major pain point that was overlooked. Ripple users had to manually conduct reconciliation tasks that took a lot of time and were prone to errors. They had to retrieve data from multiple sources and put in a lot of time to customize it based on their needs. Plus it wasn't aligned to the market standards. As a result, a lot of financial transactions were lost,  the users were frustrated with the time-consuming process. My breakthrough came with designing a reporting flow that automated the entire ordeal. This one-stop solution brought transparency, streamlined the reconciliation process, and ensured comprehensive payment tracking by improving the operating time by around 80%.  In doing so, it turned a frustrating, labor-intensive task into a seamless, reliable process. My professional journey at Amadeus, where I led the design for B2B and SaaS tools utilized by help desks at Air Canada and Southwest, serving over 30,000 airline agents, has prepared me for the challenges and opportunities at Front. The automated workflows we developed significantly enhanced the user journey and reduced agent processing time by 10 minutes, translating to approximately a 66% improvement in efficiency. Now whatever company is mentioned in the user prompt please say how this candidate is an good fit for that company. "),
#         ("user", "{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"),
#     ]
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"You are a Career advisor specializing in tech jobs - here is a profile of a candidate with their introduction: {system_prompt} How does this candidate fit for {company_input}? Please write it in first person, as if the candidate is typing the message and within 200 words. Make it as human and personalized as possible. Sound formal and relate the candidates experiences with certain projects of the company in depth. Be specific and do extensive research on the company, mostly from their website and blog posts about the mentioned company. Write it in the form of a message to the hiring manager Mr. X "),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

from langchain.tools.render import format_tool_to_openai_function
llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


import os 


#user_input = input("Please enter your query")

user_input = "Craft a story as to how this candidate's profile fit well with the mission of the company mentioned"

p=agent_executor.invoke(
{
    "input": user_input
}
)
output_text = p["output"]
#print(output_text)





  








    



