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

