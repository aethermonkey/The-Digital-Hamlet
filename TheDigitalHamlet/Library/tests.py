from django.test import TestCase
from Library.models import LibraryAgent
from autogen import UserProxyAgent, config_list_from_json, config_list_from_models


config_list = {
    config_list_from_json(env_or_file="OAI_CONFIG_LIST")

}
# Create Assistant
assistant = LibraryAgent("Librarian", llm_config=config_list)

# User Proxy
user = UserProxyAgent("User", code_execution_config=False)
user.initiate_chat(assistant, message="Hello there! How are you?")
# Library
# Initiate Conversation
