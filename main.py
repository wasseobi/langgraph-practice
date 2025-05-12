from src import graph

config = {"configurable": {"thread_id": "1"}}

if __name__ == "__main__":
    while True:
        user_input = input("🤔 ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break

        messages = {
            'messages': [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }

        graph.invoke(messages, config)
