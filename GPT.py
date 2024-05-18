'''
A "desktop app" of that converse with you using GPT.

Minimum functionality:
- no web interface
- no backend database
- implement via GPT assistant API
- double-click to start chatting, and close to stop

5/17/2024: Updated to Assistant API v2
'''

import time
from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

# connect to openai
client = OpenAI()
thread = client.beta.threads.create()

# retrieve assistant
assistant = client.beta.assistants.retrieve("asst_1xW83AWPDb52ganvqZsCMius")

def ask_assistant(user_input):
    # create thread
    thread = client.beta.threads.create()

    # add user input as message
    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = user_input
    )

    class EventHandler(AssistantEventHandler):    
        @override
        def on_text_created(self, text) -> None:
            print(f"\nassistant > ", end="", flush=True)
        
        @override
        def on_text_delta(self, delta, snapshot):
            print(delta.value, end="", flush=True)
        
        def on_tool_call_created(self, tool_call):
            print(f"\nassistant > {tool_call.type}\n", flush=True)
    
        def on_tool_call_delta(self, delta, snapshot):
            if delta.type == 'code_interpreter':
                if delta.code_interpreter.input:
                    print(delta.code_interpreter.input, end="", flush=True)
                if delta.code_interpreter.outputs:
                    print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)
 
    # Then, we use the `stream` SDK helper 
    # with the `EventHandler` class to create the Run 
    # and stream the response.
    
    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id=assistant.id,
        event_handler=EventHandler(),
    ) as stream:
        stream.until_done()

if __name__ == "__main__":
    print("\nGPT assistant is ready to chat with you! Type /bye to exit. \n")
    while True:
        user_input = input(">> ")
        if user_input == "/bye":
            break
        ask_assistant(user_input)
        print("\n")