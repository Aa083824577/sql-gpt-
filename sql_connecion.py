import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase

load_dotenv()
assert os.getenv("OPENAI_API_KEY")

db = SQLDatabase.from_uri(
    "mysql+mysqlconnector://root:root@localhost:3306/mydatabase"
)

schema = db.get_table_info()

prompt = ChatPromptTemplate.from_template("""
Based on the table schema below, write a SQL query that answers the user question.
Return ONLY the SQL query.

Schema:
{schema}

Question:
{question}

SQL Query:
""")

model = ChatOpenAI(model="gpt-4o-mini")   # Or gpt-4.1, etc.

def ask_db(question: str):
    # Step 1 → Generate SQL
    formatted = prompt.format(schema=schema, question=question)
    sql = model.invoke(formatted).content.strip()

    # Step 2 → Run SQL
    try:
        result = db.run(sql)
    except Exception as e:
        return f"SQL error: {e}\nQuery was: {sql}"
    
    # Step 3 → Return result
    return result

# Example
print(ask_db("How many costumer  are there?"))
