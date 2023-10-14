# UserProxyAgent Cheat Sheet

## Class Information

- **Class**: UserProxyAgent
- **Module**: user_proxy_agent.py
- **Path**: /plan/autogen/agentchat/user_proxy_agent.py

## Description

The `UserProxyAgent` class is a proxy agent for the user that can execute code and provide feedback to other agents. It is a subclass of `ConversableAgent` and is configured with `human_input_mode` set to "ALWAYS" and `llm_config` set to False.

## Class

### UserProxyAgent

- **Description**: A proxy agent for the user that can execute code and provide feedback to other agents.
- **Inherits**: ConversableAgent

#### Methods

- `__init__(name: str, is_termination_msg: Optional[Callable[[Dict], bool]] = None, max_consecutive_auto_reply: Optional[int] = None, human_input_mode: Optional[str] = "ALWAYS", function_map: Optional[Dict[str, Callable]] = None, code_execution_config: Optional[Union[Dict, bool]] = None, default_auto_reply: Optional[Union[str, Dict, None]] = "", llm_config: Optional[Union[Dict, bool]] = False, system_message: Optional[str] = "")`: Initializes the UserProxyAgent object.
- `get_human_input(message: Optional[str] = None) -> str`: Prompts the user for input.
- `execute_code_blocks(code_blocks: List[str]) -> List[str]`: Executes a list of code blocks and returns the results.
- `run_code(code: str) -> str`: Executes a single code block and returns the result.
- `execute_function(function_name: str, args: Optional[Dict[str, Any]] = None) -> Any`: Executes a function call and returns the result.
- `generate_init_message() -> str`: Generates the initial message when a conversation starts.
- `register_reply(reply_func: Callable[[Dict], Optional[str]])`: Registers a reply function for auto-reply.
