# SQL-GPT: Natural Language Database Query Assistant

An intelligent chatbot that converts natural language questions into SQL queries using LangChain and OpenAI's GPT models. Ask questions in plain English, and the system automatically generates safe SELECT queries, executes them on your MySQL database, and explains the results in simple terms.

## Features

- **Natural Language Processing**: Ask database questions in plain English
- **Automatic SQL Generation**: Converts your questions to safe SELECT-only queries
- **Schema-Aware**: Analyzes your database schema to generate accurate queries
- **Result Interpretation**: Provides natural language explanations of query results
- **Safety First**: Restricted to SELECT queries to prevent data modification
- **LangChain Integration**: Uses LangChain for robust AI workflow management

## Technology Stack

- **Python**
- **LangChain**: For AI workflow orchestration
- **OpenAI GPT**: Language model for query generation and result interpretation , you can use any llm you want and you can use a local hosted llm in your server to protect your data 
- **MySQL**: Database backend
- **mysql-connector-python**: Database connectivity
- **python-dotenv**: Environment variable management

## Prerequisites

- Python 3.8 or higher
- MySQL database server
- OpenAI API key

## Installation



1. Install required dependencies:
```bash
pip install langchain langchain-openai langchain-community python-dotenv mysql-connector-python
```

2. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

3. Configure your database connection in `main.py`:
```python
db_url = "mysql+mysqlconnector://username:password@localhost:3306/your_database"
```

## Usage

Run the application:
```bash
python main.py
```

Example interaction:
```
ask a question: How many users are registered in the system?

Chatbot says: Based on the query results, there are 150 users registered in your system.
```

## Project Structure

```
sql-gpt-/
├── main.py              # Main application with LangChain workflow
├── sql_connecion.py     # Database connection utilities to cheeck if there any error in the conection and it cosed by the databse systeme manager 
├── .gitignore          # Git ignore file
└── .env                # Environment variables (not tracked)
```

## How It Works

1. **User Input**: You ask a question in natural language
2. **Schema Analysis**: The system retrieves your database schema
3. **SQL Generation**: GPT generates a safe SELECT query based on the schema
4. **Query Execution**: The SQL query is executed on your database
5. **Result Interpretation**: GPT explains the results in plain language

## Security Features

- **SELECT-only queries**: Prevents data modification or deletion
- **Schema-based generation**: Ensures queries are valid for your database structure
- **Environment variable protection**: API keys stored securely in `.env` file

## Future Improvements

- [ ] Support for multiple database types (PostgreSQL, SQLite, excel , google sheets )
- [ ] Query history and caching
- [ ] Web interface using Streamlit
- [ ] Multi-turn conversations with context awareness
- [ ] Query optimization suggestions
- [ ] Export results to CSV/JSON
- [ ] find now methode because this one use the llm two times  and it analyse the entire database schema so if it a big database it gonna cost us a loot

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


## Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [OpenAI GPT](https://openai.com/)

---

⭐ If you find this project useful, please consider giving it a star!
