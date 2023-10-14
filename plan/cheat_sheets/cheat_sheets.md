# Agent Class

The `Agent` class is an abstract class for AI agent.

## Constructor

- `__init__(self, name: str)`: Initializes the agent with a name.

## Properties

- `name`: Returns the name of the agent.

## Methods

- `send(self, message: Union[Dict, str], recipient: Agent, request_reply: Optional[bool] = None)`: Sends a message to another agent.
- `receive(self, message: Union[Dict, str], sender: Agent, request_reply: Optional[bool] = None)`: Receives a message from another agent.
- `reset(self)`: Resets the agent.
- `generate_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, **kwargs) -> Union[str, Dict, None]`: Generates a reply based on the received messages.


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


# openai_utils.py Cheat Sheet

## Module Information

- **Module**: openai_utils.py
- **Path**: /plan/autogen/oai/openai_utils.py

## Description

The `openai_utils.py` module provides utility functions for working with the OpenAI API. It includes functions for getting a unique identifier of a configuration, getting a list of configs for OpenAI API calls, filtering the config list, and more.

## Functions

### get_key(config: Union[dict, list]) -> Tuple

- **Description**: Get a unique identifier of a configuration.
- **Parameters**:
  - `config` (dict or list): A configuration.
- **Returns**: A tuple that serves as a unique identifier for the configuration.

### get_config_list(api_keys: List, api_bases: Optional[List] = None, api_type: Optional[str] = None, api_version: Optional[str] = None) -> List[Dict]

- **Description**: Get a list of configs for OpenAI API calls.
- **Parameters**:
  - `api_keys` (list): The API keys for OpenAI API calls.
  - `api_bases` (list, optional): The API bases for OpenAI API calls.
  - `api_type` (str, optional): The API type for OpenAI API calls.
  - `api_version` (str, optional): The API version for OpenAI API calls.
- **Returns**: A list of configs for OpenAI API calls.

### config_list_openai_aoai(key_file_path: Optional[str] = ".", openai_api_key_file: Optional[str] = "key_openai.txt", aoai_api_key_file: Optional[str] = "key_aoai.txt", aoai_api_base_file: Optional[str] = "base_aoai.txt", exclude: Optional[str] = None) -> List[Dict]

- **Description**: Get a list of configs for OpenAI + Azure OpenAI API calls.
- **Parameters**:
  - `key_file_path` (str, optional): The path to the key files.
  - `openai_api_key_file` (str, optional): The file name of the OpenAI API key.
  - `aoai_api_key_file` (str, optional): The file name of the Azure OpenAI API key.
  - `aoai_api_base_file` (str, optional): The file name of the Azure OpenAI API base.
  - `exclude` (str, optional): The API type to exclude, "openai" or "aoai".
- **Returns**: A list of configs for OpenAI API calls.

### config_list_from_models(key_file_path: Optional[str] = ".", openai_api_key_file: Optional[str] = "key_openai.txt", aoai_api_key_file: Optional[str] = "key_aoai.txt", aoai_api_base_file: Optional[str] = "base_aoai.txt", exclude: Optional[str] = None, model_list: Optional[list] = None) -> List[Dict]

- **Description**: Get a list of configs for API calls with models in the model list.
- **Parameters**:
  - `key_file_path` (str, optional): The path to the key files.
  - `openai_api_key_file` (str, optional): The file name of the OpenAI API key.
  - `aoai_api_key_file` (str, optional): The file name of the Azure OpenAI API key.
  - `aoai_api_base_file` (str, optional): The file name of the Azure OpenAI API base.
  - `exclude` (str, optional): The API type to exclude, "openai" or "aoai".
  - `model_list` (list, optional): The model list.
- **Returns**: A list of configs for OpenAI API calls.

### config_list_gpt4_gpt35(key_file_path: Optional[str] = ".", openai_api_key_file: Optional[str] = "key_openai.txt", aoai_api_key_file: Optional[str] = "key_aoai.txt", aoai_api_base_file: Optional[str] = "base_aoai.txt", exclude: Optional[str] = None) -> List[Dict]

- **Description**: Get a list of configs for GPT-4 followed by GPT-3.5 API calls.
- **Parameters**:
  - `key_file_path` (str, optional): The path to the key files.
  - `openai_api_key_file` (str, optional): The file name of the OpenAI API key.
  - `aoai_api_key_file` (str, optional): The file name of the Azure OpenAI API key.
  - `aoai_api_base_file` (str, optional): The file name of the Azure OpenAI API base.
  - `exclude` (str, optional): The API type to exclude, "openai" or "aoai".
- **Returns**: A list of configs for OpenAI API calls.

### filter_config(config_list: List[Dict], filter_dict: Dict) -> List[Dict]

- **Description**: Filter the config list by provider and model.
- **Parameters**:
  - `config_list` (list): The config list.
  - `filter_dict` (dict, optional): The filter dict with keys corresponding to a field in each config and values corresponding to lists of acceptable values for each key.
- **Returns**: The filtered config list.

### config_list_from_json(env_or_file: str, file_location: Optional[str] = "", filter_dict: Optional[Dict[str, Union[List[Union[str, None]], Set[Union[str, None]]]]] = None) -> List[Dict]

- **Description**: Get a list of configs from a JSON parsed from an environment variable or a file.
- **Parameters**:
  - `env_or_file` (str): The environment variable name or file name.
  - `file_location` (str, optional): The file location.
  - `filter_dict` (dict, optional): The filter dict with keys corresponding to a field in each config and values corresponding to lists of acceptable values for each key.
- **Returns**: A list of configs for OpenAI API calls.


# groupchat.py Cheat Sheet

## Module Information

- **Module**: groupchat.py
- **Path**: /plan/autogen/agentchat/groupchat.py

## Description

The `groupchat.py` module provides `GroupChat` and `GroupChatManager` classes for managing a group chat with multiple agents.

## Class

### GroupChat

- **Description**: Represents a group chat with multiple agents.
- **Data Attributes**: `agents`, `messages`, `max_round`, `admin_name`
- **Properties**: `agent_names`
- **Methods**: `reset()`, `agent_by_name(name: str)`, `next_agent(agent: Agent)`, `select_speaker_msg()`, `select_speaker(last_speaker: Agent, selector: ConversableAgent)`, `_participant_roles()`

### GroupChatManager

- **Description**: Serves as a chat manager agent for managing a group chat.
- **Inherits**: ConversableAgent
- **Methods**: `__init__(groupchat: GroupChat, name: Optional[str], max_consecutive_auto_reply: Optional[int], human_input_mode: Optional[str], system_message: Optional[str], **kwargs)`, `run_chat(messages: Optional[List[Dict]], sender: Optional[Agent], config: Optional[GroupChat])`

# completion.py Cheat Sheet

## Module Information

- **Module**: completion.py
- **Path**: /plan/autogen/oai/completion.py

## Description

The `completion.py` module provides the `Completion` class for the OpenAI completion API and functions for tuning and testing the API.

## Class

### Completion

- **Description**: Represents the OpenAI completion API.
- **Inherits**: openai.Completion
- **Methods**: `create(context: Optional[Dict], use_cache: Optional[bool], config_list: Optional[List[Dict]], filter_func: Optional[Callable[[Dict, Dict, Dict], bool]], raise_on_ratelimit_or_timeout: Optional[bool], allow_format_str_template: Optional[bool], **config)`, `cost(response: dict)`, `extract_text(response: dict)`, `extract_text_or_function_call(response: dict)`, `test(data, eval_func=None, use_cache=True, agg_method="avg", return_responses_and_per_instance_result=False, logging_level=logging.WARNING, **config)`

## Helper Functions

The `completion.py` module includes helper functions for working with completions.


# AssistantAgent Class

The `AssistantAgent` class is a subclass of `ConversableAgent` and is designed to solve a task with LLM.

## Constructor

- `__init__(self, name: str, system_message: Optional[str] = DEFAULT_SYSTEM_MESSAGE, llm_config: Optional[Union[Dict, bool]] = None, is_termination_msg: Optional[Callable[[Dict], bool]] = None, max_consecutive_auto_reply: Optional[int] = None, human_input_mode: Optional[str] = "NEVER", code_execution_config: Optional[Union[Dict, bool]] = False, **kwargs)`: Initializes the `AssistantAgent` with the provided parameters.

## Properties

- `name`: Returns the name of the agent.

## Methods

- `generate_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, **kwargs) -> Union[str, Dict, None]`: Generates a reply based on the received messages.


# code_utils.py Cheat Sheet

## Module Information

- **Module**: code_utils.py
- **Path**: /home/cplan/dev/The-Digital-Hamlet/plan/autogen/code_utils.py

## Description

The `code_utils.py` module provides utility functions for working with code blocks and executing code in a Docker container.

## Functions

### infer_lang(code: str) -> str

- **Description**: Infers the language of the code.
- **Parameters**:
  - `code` (str): The code to infer the language from.
- **Returns**: The inferred language.

### extract_code(text: str, pattern: str = CODE_BLOCK_PATTERN) -> List[Tuple[str, str]]

- **Description**: Extracts code blocks from a text.
- **Parameters**:
  - `text` (str): The text to extract code blocks from.
  - `pattern` (str, optional): The regular expression pattern for finding the code block. Defaults to CODE_BLOCK_PATTERN.
- **Returns**: A list of tuples, each containing the language and the code.

### execute_code(
    code: Optional[str] = None,
    timeout: Optional[int] = None,
    filename: Optional[str] = None,
    work_dir: Optional[str] = None,
    use_docker: Optional[Union[List[str], str, bool]] = docker is not None,
    lang: Optional[str] = "python",
) -> Tuple[int, str, str]

- **Description**: Executes code in a Docker container.
- **Parameters**:
  - `code` (str, optional): The code to execute. Defaults to None.
  - `timeout` (int, optional): The maximum execution time in seconds. Defaults to None.
  - `filename` (str, optional): The file name to save the code or where the code is stored when `code` is None. Defaults to None.
  - `work_dir` (str, optional): The working directory for the code execution. Defaults to None.
  - `use_docker` (Union[List[str], str, bool], optional): The docker image to use for code execution. Defaults to docker is not None.
  - `lang` (str, optional): The language of the code. Defaults to "python".
- **Returns**: A tuple containing the exit code, the output logs, and the Docker image name (if Docker is used).

### generate_assertions(definition: str, **config) -> Tuple[str, float]

- **Description**: Generates assertions for a function.
- **Parameters**:
  - `definition` (str): The function definition.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.
- **Returns**: A tuple containing the generated assertions and the cost of the generation.

### improve_function(file_name, func_name, objective, **config)

- **Description**: (Work in progress) Improves the function to achieve the objective.
- **Parameters**:
  - `file_name` (str): The name of the file containing the function.
  - `func_name` (str): The name of the function to improve.
  - `objective` (str): The objective to achieve.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.

### improve_code(files, objective, suggest_only=True, **config)

- **Description**: Improves the code to achieve a given objective.
- **Parameters**:
  - `files` (list): A list of file names containing the source code.
  - `objective` (str): The objective to achieve.
  - `suggest_only` (bool): Whether to return only the suggestions or the improved code. Defaults to True.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.

### generate_code(pattern: str = CODE_BLOCK_PATTERN, **config) -> Tuple[str, float]

- **Description**: Generates code.
- **Parameters**:
  - `pattern` (str, optional): The regular expression pattern for finding the code block. Defaults to CODE_BLOCK_PATTERN.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.
- **Returns**: A tuple containing the generated code and the cost of the generation.

### generate_assertions(definition: str, **config) -> Tuple[str, float]

- **Description**: Generates assertions for a function.
- **Parameters**:
  - `definition` (str): The function definition.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.
- **Returns**: A tuple containing the generated assertions and the cost of the generation.

### eval_function_completions(
    responses: List[str],
    definition: str,
    test: Optional[str] = None,
    entry_point: Optional[str] = None,
    assertions: Optional[Union[str, Callable[[str], Tuple[str, float]]]] = None,
    timeout: Optional[float] = 3,
    use_docker: Optional[bool] = True,
) -> Dict

- **Description**: Selects a response from a list of responses for the function completion task and evaluates if the task is successful using a gold test.
- **Parameters**:
  - `responses` (list): The list of responses.
  - `definition` (str): The input definition.
  - `test` (str, optional): The test code. Defaults to None.
  - `entry_point` (str, optional): The name of the function. Defaults to None.
  - `assertions` (Union[str, Callable], optional): The assertion code or an assertion generator. Defaults to None.
  - `timeout` (float, optional): The timeout for executing the code. Defaults to 3.
  - `use_docker` (bool, optional): Whether to use Docker for code execution. Defaults to True.

### implement(
    definition: str,
    configs: Optional[List[Dict]] = None,
    assertions: Optional[Union[str, Callable[[str], Tuple[str, float]]]] = generate_assertions,
) -> Tuple[str, float]

- **Description**: Implements a function from a definition.
- **Parameters**:
  - `definition` (str): The function definition.
  - `configs` (list, optional): The list of configurations for completion. Defaults to None.
  - `assertions` (Union[str, Callable], optional): The assertion code or an assertion generator. Defaults to generate_assertions.
- **Returns**: A tuple containing the implementation, the cost of the implementation, and the index of the configuration.

## Constants

### DEFAULT_MODEL

- **Description**: The default model for code generation.

### FAST_MODEL

- **Description**: The fast model for code generation.

### CODE_BLOCK_PATTERN

- **Description**: The regular expression pattern for finding a code block.

### WORKING_DIR

- **Description**: The working directory for code execution.

### UNKNOWN

- **Description**: The default value for an unknown code block.

### TIMEOUT_MSG

- **Description**: The message displayed when code execution times out.

### DEFAULT_TIMEOUT

- **Description**: The default timeout for code execution.

## Docker

The `code_utils.py` module uses Docker for code execution. If Docker is not installed, the module falls back to executing the code in the current environment.


# MathUserProxyAgent Class

This class is a subclass of `UserProxyAgent` and is designed to handle math problems.

## Constructor

- `__init__`: Initializes the `MathUserProxyAgent`.

## Methods

- `_is_termination_msg_mathchat`: Checks if a message is a termination message.
- `_add_print_to_last_line`: Adds `print()` to the last line of a string.
- `_remove_print`: Removes all `print` statements from a string.
- `generate_init_message`: Generates a prompt for the assistant agent with the given problem and prompt.
- `_generate_math_reply`: Generates an auto reply for math problems.


# retrieve_utils.py Cheat Sheet

## Module Information

- **Module**: retrieve_utils.py
- **Path**: /home/cplan/dev/The-Digital-Hamlet/plan/autogen/retrieve_utils.py

## Description

The `retrieve_utils.py` module provides utility functions for retrieving and processing text data from various sources.

## Functions

### num_tokens_from_text(text: str, model: str = "gpt-3.5-turbo-0613", return_tokens_per_name_and_message: bool = False) -> Union[int, Tuple[int, int, int]]

- **Description**: Returns the number of tokens used by a text.
- **Parameters**:
  - `text` (str): The text to count tokens from.
  - `model` (str, optional): The language model to use. Defaults to "gpt-3.5-turbo-0613".
  - `return_tokens_per_name_and_message` (bool, optional): Whether to return the number of tokens per name and message. Defaults to False.
- **Returns**: The number of tokens used by the text.

### num_tokens_from_messages(messages: dict, model: str = "gpt-3.5-turbo-0613") -> int

- **Description**: Returns the number of tokens used by a list of messages.
- **Parameters**:
  - `messages` (dict): The list of messages.
  - `model` (str, optional): The language model to use. Defaults to "gpt-3.5-turbo-0613".
- **Returns**: The number of tokens used by the messages.

### split_text_to_chunks(text: str, max_tokens: int = 4000, chunk_mode: str = "multi_lines", must_break_at_empty_line: bool = True, overlap: int = 10) -> List[str]

- **Description**: Splits a long text into chunks of maximum tokens.
- **Parameters**:
  - `text` (str): The text to split into chunks.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
  - `overlap` (int, optional): The number of overlapping tokens between chunks. Defaults to 10.
- **Returns**: A list of text chunks.

### split_files_to_chunks(files: list, max_tokens: int = 4000, chunk_mode: str = "multi_lines", must_break_at_empty_line: bool = True) -> List[str]

- **Description**: Splits a list of files into chunks of maximum tokens.
- **Parameters**:
  - `files` (list): The list of file paths.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
- **Returns**: A list of text chunks.

### get_files_from_dir(dir_path: str, types: list = TEXT_FORMATS, recursive: bool = True) -> List[str]

- **Description**: Returns a list of all the files in a given directory.
- **Parameters**:
  - `dir_path` (str): The directory path.
  - `types` (list, optional): The list of file types to include. Defaults to TEXT_FORMATS.
  - `recursive` (bool, optional): Whether to search recursively. Defaults to True.
- **Returns**: A list of file paths.

### get_file_from_url(url: str, save_path: str = None) -> str

- **Description**: Downloads a file from a URL.
- **Parameters**:
  - `url` (str): The URL of the file.
  - `save_path` (str, optional): The path to save the downloaded file. Defaults to None.
- **Returns**: The path of the downloaded file.

### is_url(string: str) -> bool

- **Description**: Returns True if the string is a valid URL.
- **Parameters**:
  - `string` (str): The string to check.
- **Returns**: True if the string is a valid URL, False otherwise.

### create_vector_db_from_dir(
    dir_path: str,
    max_tokens: int = 4000,
    client: API = None,
    db_path: str = "/tmp/chromadb.db",
    collection_name: str = "all-my-documents",
    get_or_create: bool = False,
    chunk_mode: str = "multi_lines",
    must_break_at_empty_line: bool = True,
    embedding_model: str = "all-MiniLM-L6-v2",
)

- **Description**: Creates a vector database from all the files in a given directory.
- **Parameters**:
  - `dir_path` (str): The directory path.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `client` (API, optional): The ChromaDB client. Defaults to None.
  - `db_path` (str, optional): The path to the ChromaDB database. Defaults to "/tmp/chromadb.db".
  - `collection_name` (str, optional): The name of the collection. Defaults to "all-my-documents".
  - `get_or_create` (bool, optional): Whether to get or create the collection. Defaults to False.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
  - `embedding_model` (str, optional): The embedding model to use. Defaults to "all-MiniLM-L6-v2".

### query_vector_db(
    query_texts: List[str],
    n_results: int = 10,
    client: API = None,
    db_path: str = "/tmp/chromadb.db",
    collection_name: str = "all-my-documents",
    search_string: str = "",
    embedding_model: str = "all-MiniLM-L6-v2",
) -> Dict[str, List[str]]

- **Description**: Queries a vector database.
- **Parameters**:
  - `query_texts` (List[str]): The list of query texts.
  - `n_results` (int, optional): The number of results to retrieve. Defaults to 10.
  - `client` (API, optional): The ChromaDB client. Defaults to None.
  - `db_path` (str, optional): The path to the ChromaDB database. Defaults to "/tmp/chromadb.db".
  - `collection_name` (str, optional): The name of the collection. Defaults to "all-my-documents".
  - `search_string` (str, optional): The search string to filter the results. Defaults to "".
  - `embedding_model` (str, optional): The embedding model to use. Defaults to "all-MiniLM-L6-v2".

## Constants

### TEXT_FORMATS

- **Description**: The list of supported text file formats.

## Helper Functions

The `retrieve_utils.py` module also includes several helper functions for working with files and URLs. These functions are used internally and may not be directly called by the user.


# math_utils.py

This module provides functions for solving math problems and evaluating math responses.

## Functions

- `solve_problem(problem: str, **config) -> str`: Solves the math problem.
- `get_answer(solution: Optional[str]) -> Optional[str]`: Extracts the answer from the solution string.
- `is_equiv(str1: Optional[str], str2: Optional[str]) -> float`: Checks if two math strings are equivalent.
- `is_equiv_chain_of_thought(str1: str, str2: str) -> float`: Checks if two math strings are equivalent after stripping the solution.
- `voting_counts(responses)`: Counts the votes for each response.
- `eval_math_responses(responses, solution=None, **args)`: Evaluates the math responses and calculates success metrics.

## Constants

- `_MATH_PROMPT`: The prompt for solving a math problem.
- `_MATH_CONFIG`: The configuration for solving a math problem.
- `_STRIP_STRING_FUNCTIONS`: A list of helper functions for stripping math strings.


