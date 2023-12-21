import os
from langchain.utilities import WikipediaAPIWrapper
from langchain.utilities import PythonREPL
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.agents import initialize_agent
from llm import setup_llm


# llm = OpenAI(openai_api_key="YOUR_API_KEY")
llm = setup_llm()


wikipedia = WikipediaAPIWrapper()
def truncWikipedia(prompt):
        v = wikipedia.run(prompt)
        return v[0:128]

python_repl = PythonREPL()

search = DuckDuckGoSearchRun()
def truncDuckDuckGo(prompt):
        v = search.run(prompt)
        return v[0:128]







tools = []

python_repl_tool = Tool(
        name = "python repl",
        func=python_repl.run,
        description="useful for when you need to use python to answer a question. You should input python code"
    )

wikipedia_tool = Tool(
    name='wikipedia',
    func= truncWikipedia,
    description="Useful for when you need to look up a topic, country or person on wikipedia"
)

duckduckgo_tool = Tool(
    name='DuckDuckGo Search',
    func= truncDuckDuckGo,
    description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
)

# tools.append(python_repl_tool)
tools.append(duckduckgo_tool)
tools.append(wikipedia_tool)

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=6,
    handle_parsing_errors=True
)


# x = zero_shot_agent.run("What is 17*6?")
x = zero_shot_agent.run("When was President Barak Obama born?")
print(x)

x = zero_shot_agent.run("How old is Barack Obama?")
print(x)





