'''
A "desktop app" of that converse with you using GPT.

Minimum functionality:
- no web interface
- no backend database
- implement via GPT assistant API
- double-click to start chatting, and close to stop
'''

import time
from openai import OpenAI

# connect to openai
client = OpenAI()
thread = client.beta.threads.create()

def ask_assistant(user_input):
    # user input
    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = user_input
    )

    #thread_messages = client.beta.threads.messages.list(thread.id)
    #print(thread_messages.data)

    # run assistant
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = "asst_1xW83AWPDb52ganvqZsCMius"
    )

    # check run status
    while (run.status != "completed"):
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )

    # get assistant response
    response = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    return response.data[0].content[0].text.value

if __name__ == "__main__":
    print("\nGPT assistant is ready to chat with you! Type /bye to exit. \n")
    while True:
        user_input = input(">> ")
        if user_input == "/bye":
            break
        response = ask_assistant(user_input)
        print("\n" + response + "\n")