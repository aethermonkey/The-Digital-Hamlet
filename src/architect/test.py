import autogen
from autogen import ConversableAgent, UserProxyAgent
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant = ConversableAgent("assistant")
user_proxy = UserProxyAgent("user_proxy")
user_proxy.initiate_chat(assistant, message="As a test, please write a small script that uses sh tree")