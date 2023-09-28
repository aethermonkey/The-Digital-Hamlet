import os
import sys
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent
import autogen
import openai
from IPython import get_ipython


load_dotenv()

# Environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)

# config_list = [
#     {
#         'model': 'gpt-4',
#         'api_key': openai_api_key,
#     },
#     {
#         'seed': 42,
#         'temperature': 0.5,
#     }
# ]

llm_config = {
        "functions": [
        {
            "name": "python",
            "description": "run cell in ipython and return the execution result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "cell": {
                        "type": "string",
                        "description": "Valid Python cell to execute.",
                    }
                },
                "required": ["cell"],
            },
        },
        {
            "name": "sh",
            "description": "run a shell script and return the execution result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": "Valid shell script to execute.",
                    }
                },
                "required": ["script"],
            },
        },
    ],
    "config_list": config_list,
    "request_timeout": 120,
}
with open("src/architect/architect_init.prompt", "r") as f:
    architect_init = f.read()

with open ("src/architect/data_store/context.txt", "r") as f:
    context = f.read()
# system_message = architect_init + """\n And for context, here is a summary of our last conversation, care of Anthropics Claude! \n" + context + "\nFor coding tasks, only use the functions you have been provided with."""

system_message = """\For coding tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."""

assistant = AssistantAgent(
    system_message= system_message,
    name="The Architect",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg= lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "bench"},
)
# define functions according to the function desription
def exec_python(cell):
    ipython = get_ipython()
    result = ipython.run_cell(cell)
    log = str(result.result)
    if result.error_before_exec is not None:
        log += f"\n{result.error_before_exec}"
    if result.error_in_exec is not None:
        log += f"\n{result.error_in_exec}"
    return log

def exec_sh(script):
    return user_proxy.execute_code_blocks([("sh", script)])

# register the functions
user_proxy.register_function(
    function_map={
        "python": exec_python,
        "sh": exec_sh,
    }
)
if __name__ == "__main__":
    user_proxy.initiate_chat(assistant, message="""Just a test, execute the tree command on the base dir of the project""")
    