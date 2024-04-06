from langchain_community.document_loaders import TextLoader

import os
os.environ['OPENAI_API_KEY'] = "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"

loader = TextLoader("/Users/samriddhoghosh/Desktop/Early/doc.txt")
documents = loader.load()

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)git 
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

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"You are a message analysing beast. You can analyse messages very well and extract actionable to-do items for each particpant in the conversation"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

#prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.messages

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

from langchain.agents import AgentExecutor, create_openai_tools_agent

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# result = agent_executor.invoke({"input": "hi, im bob"})

# result["output"]

#user_input = input("Please enter some text: ")
user_input = " My name is Jules and can you give me a list of actionable todo items assigned to me from this conversation"

result = agent_executor.invoke(
    {
        "input": user_input
    }
)
resultstr = str(result)
#print(result)
#result["output"]

# prompt2 = ChatPromptTemplate.from_messages(
#     [
#         ("system", f"You are a message analysing beast. In this case, you have a set of to do items: can you make two lists, one where the to-do is time dependent or has an immediate timeline and the other list is where the todo has a verb/software mentioned "),
#         ("user", "{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"),
#     ]
# )

#user_input2 = "You are a message analysing beast. This is the context: {result} In this case, you have a set of to do items: can you make two lists, one where the to-do is time dependent that means any action item that has time mentioned, make sure in the output list you mention the time specifically and the other list is where the todo has a verb/software mentioned. The two lists show be mutually exclusive and there must not be any, i repeat any overlap of action items. If you can club 2 action items that belong to the same person do that. at the end just give me two lists.  "
user_input2 = "Read through the message conversation and give me the action items assigned to Jules have have a specific timeline or deadline. Please mention the time by which the work needs to be done"

result2 = agent_executor.invoke(
    {
        "input": user_input2
    }
)
#print(result2['output'])

# Given string output
#output_string = "Action items assigned to Jules with specific timeline:\n1. Compile and ensure the PPT is ready for review by 2 PM today. (Timeline: By 2 PM today)\n2. Prepare speaker notes to help during the presentation. (Timeline: Before the rehearsal at 4 PM today)"

# Split the string based on numbered list format
action_items = result2['output'].split('\n')

# Divide into two separate strings with two separate pointers
string_1 = '\n'.join(action_items[:2])
string_2 = '\n'.join(action_items[2:])



# Displaying the divided strings
print("String 1:")
print(string_1)
print("\nString 2:")
print(string_2)


#--------------------------Notification code



from notifypy import Notify

notification = Notify()
notification.title = "Reminder 1"
notification.message = string_1
notification.audio = "/Users/samriddhoghosh/Desktop/Early/beep-07a.wav"
notification.icon = "/Users/samriddhoghosh/Desktop/Early/LogoNudge.png"
notification.application_name = "Nudge"


notification.send()

notification.title = "Reminder 2"
notification.message = string_2
notification.audio = "/Users/samriddhoghosh/Desktop/Early/beep-07a.wav"
notification.icon = "/Users/samriddhoghosh/Desktop/Early/LogoNudge.png"
notification.application_name = "Nudge"

notification.send()





# def extract_actionable_items(result2):
#     actionable_items = []clear
#     for key, value in result2.items():
#         if isinstance(value, str):
#             start_index = value.find('**')
#             end_index = value.find('**', start_index + 2)
#             if start_index != -1 and end_index != -1:
#                 actionable_items.append(value[start_index + 2:end_index])
#     return actionable_items



# actionable_items = extract_actionable_items(result2)
# print("Actionable Items:")
# for item in actionable_items:
#     print(item)

#result["output"]

# action_items_array = []

# #----------------------------#
# action_items = []
# for line in str(result2).split('\n'):
#     if '**' in line:
#         start_index = line.find('**') + 2
#         end_index = line.rfind('**')
#         action_item = line[start_index:end_index]

#         print (action_item)
#         print ()

       # action_items.append(action_item)

       # action_items_array = action_items_array + action_items

# Converting to string array


#print(action_items_array)



















# import pandas as pd
# import re

# # Provided text
# #text = """Based on the provided context, I have extracted the following action items:\n\n**Time-Dependent To-Do List:**\n1. Amanda: Connect with the client to confirm tomorrow’s presentation time.\n2. Amanda: Finalize the PPT for the client presentation by EOD today.\n3. Amanda: Review the finalized PPT and send it to Sam for final approval by 3 PM.\n4. Jules: Ensure the PPT is ready for review by 2 PM.\n5. Amanda: Schedule a rehearsal call for 4 PM today.\n\n**Verb/Software Mentioned To-Do List:**\n1. Jules: Add the project timeline and next steps to the PPT.\n2. Zach: Shorten the video clip to keep the presentation concise.\n3. Zach: Integrate the necessary data for the market analysis section into the PPT.\n4. Jules: Oversee the alignment of the presentation with the client's brand guidelines.\n5. Zach: Add interactive elements like a short video clip and infographics to the presentation.\n6. Jules: Compile everything and ensure it's ready for review.\n7. Zach: Send his sections to Jules before noon.\n8. Sam: Schedule a rehearsal call after the presentation is approved.\n9. Jules: Prepare speaker notes for the presentation.\n10. Zach: Work on a FAQ section for the presentation.\n\nThese lists are mutually exclusive with no overlap of action items. Let me know if you need any further assistance."""

# # Regular expression to extract action items and headers
# pattern = r'\d+\.\s*(.+):\s*(.+)\.'

# # Initialize lists to store extracted data
# headers = []
# actions = []

# # Find all matches in the text
# matches = re.findall(pattern, str(result2))

# # Iterate over matches and extract headers and actions
# for match in matches:
#     headers.append(match[0])
#     actions.append(match[1])

# # Create a DataFrame
# df = pd.DataFrame({
#     'Header': headers,
#     'Action': actions
# })

# # Display the DataFrame
# print(df)
# df.to_csv('data.csv', index=False)