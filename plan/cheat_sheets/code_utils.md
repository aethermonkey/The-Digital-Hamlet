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

