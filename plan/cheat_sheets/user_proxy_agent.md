# UserProxyAgent

- **Path**: /plan/autogen/agentchat/user_proxy_agent.py
- **Description**: A proxy agent for the user that can execute code and provide feedback to other agents.
- **Inherits**: ConversableAgent

## Methods

- `__init__(name, is_termination_msg=None, max_consecutive_auto_reply=None, human_input_mode="ALWAYS", function_map=None, code_execution_config=None, default_auto_reply="", llm_config=False, system_message="")`: Initializes the UserProxyAgent.
- `get_human_input(message=None)`: Prompts the user for input.
- `execute_code_blocks(code_blocks)`: Executes a list of code blocks and returns the results.
- `run_code(code)`: Executes a single code block and returns the result.
- `execute_function(function_name, args=None)`: Executes a function call and returns the result.
- `generate_init_message()`: Generates the initial message when a conversation starts.
- `register_reply(reply_func)`: Registers a reply function for auto-reply.
