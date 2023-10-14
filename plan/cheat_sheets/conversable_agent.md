# conversable_agent.py Cheat Sheet

## Module Information

- **Module**: conversable_agent.py
- **Path**: /plan/autogen/agentchat/conversable_agent.py

## Description

The `conversable_agent.py` module provides a class `ConversableAgent` that serves as a base class for generic conversable agents. These agents can be configured as assistant or user proxies and can engage in conversations by sending and receiving messages.

## Class

### ConversableAgent

- **Description**: A class for generic conversable agents.
- **Inherits**: Agent

#### Properties

- `system_message`: The system message for the ChatCompletion inference.

#### Methods

- `__init__(self, name: str, system_message: Optional[str] = "You are a helpful AI Assistant.", is_termination_msg: Optional[Callable[[Dict], bool]] = None, max_consecutive_auto_reply: Optional[int] = None, human_input_mode: Optional[str] = "TERMINATE", function_map: Optional[Dict[str, Callable]] = None, code_execution_config: Optional[Union[Dict, bool]] = None, llm_config: Optional[Union[Dict, bool]] = None, default_auto_reply: Optional[Union[str, Dict, None]] = "")`: Initializes the ConversableAgent object.
- `register_reply(self, trigger: Union[Type[Agent], str, Agent, Callable[[Agent], bool], List], reply_func: Callable, position: Optional[int] = 0, config: Optional[Any] = None, reset_config: Optional[Callable] = None)`: Registers a reply function.
- `update_system_message(self, system_message: str)`: Updates the system message.
- `update_max_consecutive_auto_reply(self, value: int, sender: Optional[Agent] = None)`: Updates the maximum number of consecutive auto replies.
- `max_consecutive_auto_reply(self, sender: Optional[Agent] = None) -> int`: Returns the maximum number of consecutive auto replies.
- `chat_messages(self) -> Dict[str, List[Dict]]`: Returns a dictionary of conversations from name to list of ChatCompletion messages.
- `last_message(self, agent: Optional[Agent] = None) -> Dict`: Returns the last message exchanged with the agent.
- `use_docker(self) -> Union[bool, str, None]`: Returns the value indicating whether to use docker for code execution.
- `_append_oai_message(self, message: Union[Dict, str], role, conversation_id: Agent) -> bool`: Appends a message to the ChatCompletion conversation.
- `send(self, message: Union[Dict, str], recipient: Agent, request_reply: Optional[bool] = None, silent: Optional[bool] = False) -> bool`: Sends a message to another agent.
- `a_send(self, message: Union[Dict, str], recipient: Agent, request_reply: Optional[bool] = None, silent: Optional[bool] = False) -> bool`: (async) Sends a message to another agent.
- `_print_received_message(self, message: Union[Dict, str], sender: Agent)`: Prints the received message.
- `_process_received_message(self, message, sender, silent)`: Processes the received message.
- `receive(self, message: Union[Dict, str], sender: Agent, request_reply: Optional[bool] = None, silent: Optional[bool] = False)`: Receives a message from another agent.
- `a_receive(self, message: Union[Dict, str], sender: Agent, request_reply: Optional[bool] = None, silent: Optional[bool] = False)`: (async) Receives a message from another agent.
- `_prepare_chat(self, recipient, clear_history)`: Prepares for a chat with the recipient agent.
- `initiate_chat(self, recipient: "ConversableAgent", clear_history: Optional[bool] = True, silent: Optional[bool] = False, **context)`: Initiates a chat with the recipient agent.
- `a_initiate_chat(self, recipient: "ConversableAgent", clear_history: Optional[bool] = True, silent: Optional[bool] = False, **context)`: (async) Initiates a chat with the recipient agent.
- `reset(self)`: Resets the agent.
- `stop_reply_at_receive(self, sender: Optional[Agent] = None)`: Stops the reply at receive for the sender.
- `reset_consecutive_auto_reply_counter(self, sender: Optional[Agent] = None)`: Resets the consecutive auto reply counter for the sender.
- `clear_history(self, agent: Optional[Agent] = None)`: Clears the chat history of the agent.
- `generate_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, exclude: Optional[List[Callable]] = None) -> Union[str, Dict, None]`: Generates a reply based on the conversation history and the sender.
- `a_generate_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, exclude: Optional[List[Callable]] = None) -> Union[str, Dict, None]`: (async) Generates a reply based on the conversation history and the sender.
- `get_human_input(self, prompt: str) -> str`: Gets human input.
- `run_code(self, code, **kwargs)`: Runs the code and returns the result.
- `execute_code_blocks(self, code_blocks)`: Executes the code blocks and returns the result.
- `execute_function(self, func_call)`: Executes a function call and returns the result.
- `generate_init_message(self, **context) -> Union[str, Dict]`: Generates the initial message for the agent.
- `register_function(self, function_map: Dict[str, Callable])`: Registers functions to the agent.

## Constants

### DEFAULT_CONFIG

- **Description**: The default configuration for the ConversableAgent class.

### MAX_CONSECUTIVE_AUTO_REPLY

- **Description**: The maximum number of consecutive auto replies.

### DEFAULT_MODEL

- **Description**: The default model for ChatCompletion inference.

### UNKNOWN

- **Description**: The unknown language identifier.

### _MATH_PROMPT

- **Description**: The prompt for solving a math problem.

### _MATH_CONFIG

- **Description**: The configuration for solving a math problem.

### _STRIP_STRING_FUNCTIONS

- **Description**: A list of helper functions for stripping math strings.

