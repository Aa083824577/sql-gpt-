import os 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv()
assert os.getenv("OPENAI_API_KEY")

template = """
You are a SQL expert. Based only on the schema below,
generate a safe SELECT-only SQL query that answers the user's question.
Schema:
{schema}

User question: {question}

SQL:
"""

answer_template = """
You are a helpful assistant. 
The user asked a question. 
You already generated a SQL query and executed it.
Now explain the result in simple natural language.

Question: {question}
SQL Query: {query}
SQL Result: {result}

Final Answer:
"""

answer_prompt = ChatPromptTemplate.from_template(answer_template)
prompt = ChatPromptTemplate.from_template(template)


# init the sql database
db_url = "mysql+mysqlconnector://root:root@localhost:3306/mydatabase"
db = SQLDatabase.from_uri(db_url)


def get_schema(_):
    return db.get_table_info()

# llm
llm = ChatOpenAI()
# build the chain 
sql_chain = (
     RunnablePassthrough.assign(schema=get_schema)
     | prompt
     | llm.bind(stop="\nSQL Result:")
     | StrOutputParser()
)

user_question = input("ask a quation")
# use the chain that generat the sql query 
query = sql_chain.invoke({"question": user_question})

# excute the sql query
result = db.run(query)

# use the chain that generat the anwser 
final_chain = answer_prompt | llm | StrOutputParser()
answer = final_chain.invoke({
    "question": user_question,
    "query": query,
    "result": result
})

print("Chatbot says:", answer)
