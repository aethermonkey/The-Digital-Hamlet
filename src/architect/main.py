import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent
import autogen
import openai


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

config_list = [
    {
        'model': 'gpt-4',
        'api_key': openai_api_key,
    },
    {
        'seed': 42,
        'temperature': 0.9,
    }
]
with open("src/architect/test_bench/spec.txt", "r") as f:
    specs = f.read()

assistant = AssistantAgent(
    system_message="You are a helpful software engineer. Project: " + specs,
    name="The Architect",
    llm_config=config_list,
)

user_proxy = UserProxyAgent(
    name="USER",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "src/architect/test_bench",    
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
)

if __name__ == "__main__":
    user_proxy.initiate_chat(assistant, message="""let's start planning the hamlet?""")
    