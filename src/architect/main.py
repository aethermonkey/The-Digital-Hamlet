import os
import sys
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent
import autogen
import openai
from helper_functions.arch_utils import list_files, get_system_info
import platform
# from IPython import get_ipython


load_dotenv()

# Environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        # "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
        "model": ["gpt-3.5-turbo"],
    },
)


with open(os.path.join(os.path.dirname(__file__), "data_store/architect_init.prompt"), "r") as f:
    architect_init = f.read()

with open (os.path.join(os.path.dirname(__file__), "data_store/context.txt"), "r") as f:
    context = f.read()

system_message = architect_init + "\n" + context

assistant = AssistantAgent(
    name="The Architect",
    system_message=system_message,
    llm_config={
        "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    }, 
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg= lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "../../",
        "use_docker": False,
    },
)

if __name__ == "__main__":
    # chat = user_proxy.initiate_chat(assistant, context=context, clear_history=False, message="""how is our development going?""")
    # print(chat)
    print(get_system_info())
    print(list_files('/home/cplan/dev/The-Digital-Hamlet/'))