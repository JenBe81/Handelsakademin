import argparse
from modules.llm_interface import invoke, content_step1
from modules.database import execute_sql, get_cursor_and_connection
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description="SQLite Database Chat")
parser.add_argument("--name", type=str, default="No name", help="Your name for the chat prompt")
args = parser.parse_args()

def print_help():
    help_text = """
Each request must start with either keyword 'get' or 'set'.
- 'Get' means you want to retrieve something from the database.
- 'Set' means you want to enter, or change, something in the database.

That should be followed by a type. Legitimate types are:
- 'meeting'
- 'note'
- 'diary'
- 'task'.

After that, you can write in plain text what you want to do.

For example: "get task show me all tasks".
    """
    print(help_text)

def format_and_print_output(raw_result):
    result_list = json.loads(raw_result)

    for item in result_list:
        print(f"\n** {item['title']} **")

        content = json.loads(item["content"]) if "{" in item["content"] else {"content": item["content"]}
        for key, value in content.items():
            print(f"  -{key}: {value}")
        
        print(f"  -tags: {item['tags']}\n")

def load_input(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main(name="No Name"):

    #Connect to the database
    c, conn = get_cursor_and_connection()

    print(f"\nWelcome to the SQLite Database Chat, {name}! Type 'quit' to exit.\n")

    user_question = ""
    context = None
    while True:
        user_question = input(f"\n{name}: ")

        # Stop conditions
        if user_question.lower() in ["quit", "exit", "q"]:
            print(f"\nGood bye, {name}!")
            break
        elif user_question.lower() == "help":
            print_help()
            continue

        first_word = user_question.split()[0].lower()
        if first_word in ["get", "set"]:
            # Handle first step questions
            words = user_question.split()

            if len(words) > 1 and words[-1].endswith(".txt"):
                file_path = words[-1]
                file_content = load_input(file_path)

                if file_content is None:
                    continue

                updated_content = content_step1.format(user_question=file_content)
            else:
                updated_content = content_step1.format(user_question=user_question)
            
            try:
                sql_command = invoke(updated_content)
                print(f"\Generated SQL Command: {sql_command}")
            except Exception as e:
                print("\nError:", e)
                continue

            result = execute_sql(c, conn, sql_command)

            if sql_command.startswith("SELECT"):
                format_and_print_output(result)

            # Update the context for possible follow-up questions
            context = f"User question: {user_question}\nResult: {result}"

        else:
            # Handle second step (follow-up) questions
            if context:

                # Prepare the content for follow-up questions
                content_step2 = f"Answer this question: {user_question}\n\nGiven the below previous question and answer context:\n{context}"
                
                try:
                    response = invoke(content_step2)
                except Exception as e:
                    print("\nError:", e)
                    continue

                print(response)

                # Update the context with the new user_question and response
                context += f"\n\nUser question: {user_question}\nResult: {response}"
                    
            else:
                print("Please start with either 'get' or 'set'")

# Call the main function when the script is executed
if __name__ == "__main__":
    main(args.name)