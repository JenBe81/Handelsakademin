import json
import requests

# Set up Open AI ChatGPT LLM
AZURE_OPENAI_API_KEY = "Private so not shared"

content_step1 = f"""You are an expert in SQL commands and SQLite databases. Interpret the below user query and convert it to the appropriate SQL command. Reply only with SQL command and nothing else.
        
        Table documents in the database looks like this:
        documents (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        
        User queries should start with either 'get' or 'set'. 'Get' means the user wants to retrieve something from the documents table, and 'set' means the user wants to insert something into the documents table.
        
        Next word should be the type which should be either 'meeting', 'note', 'diary' or 'task'. After that comes the content. From the content, identify a proper title and tags. Make sure to preserve the singular/plural form provided in the user query when generating the SQL command.
        
        Examples:
        1. User Query: 'set task Update release 4.34 gantt chart and upload to RLCF Sharepoint by end of week'
           Generated SQL Command: INSERT INTO documents (type, title, content, tags) VALUES ("task", "Update release 4.34 gantt chart", "Update release 4.34 gantt chart and upload to RLCF Sharepoint by end of week", "gantt, RLCF, Sharepoint, release 4.34")
        
        2. User Query: 'get all tasks'
           Generated SQL Command: SELECT * FROM documents WHERE type = "task"

        User query: {{user_question}}
        """

def invoke(content=None):

        body = {
            "messages": [
                {
                    "role": "assistant",
                    "content": content
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "api-key": AZURE_OPENAI_API_KEY
        }
        url = "https://openai-eaus-dev-002.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2023-03-15-preview"
        response = requests.post(url, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            result = response.json()["choices"][0]["message"]["content"].replace("\n", " ")
            reply = result.strip()
        
        else:
            print("Status Code:", response.status_code)
            print("API Response:", response.text)
            raise Exception(f"Error {response.status_code}: {response.text}")
        
        return reply