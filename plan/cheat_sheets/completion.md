# completion.py Cheat Sheet

## Module Information

- **Module**: completion.py
- **Path**: /plan/autogen/oai/completion.py

## Description

The `completion.py` module provides a class `Completion` that represents the OpenAI completion API. It also includes functions for tuning and testing the completion API.

## Class

### Completion

- **Description**: A class for the OpenAI completion API.
- **Inherits**: openai.Completion

#### Methods

- `create(context: Optional[Dict] = None, use_cache: Optional[bool] = True, config_list: Optional[List[Dict]] = None, filter_func: Optional[Callable[[Dict, Dict, Dict], bool]] = None, raise_on_ratelimit_or_timeout: Optional[bool] = True, allow_format_str_template: Optional[bool] = False, **config) -> Dict`: Makes a completion for a given context.
- `cost(response: dict) -> float`: Computes the cost of an API call.
- `extract_text(response: dict) -> List[str]`: Extracts the text from a completion response.
- `extract_text_or_function_call(response: dict) -> List[str]`: Extracts the text or function calls from a completion response.
- `test(data, eval_func=None, use_cache=True, agg_method="avg", return_responses_and_per_instance_result=False, logging_level=logging.WARNING, **config) -> Union[Dict, Tuple[Dict, List[Dict], List[List[str]]]]`: Evaluates the responses created with the config for the OpenAI API call.

## Helper Functions

The `completion.py` module also includes several helper functions for working with completions. These functions are used internally and may not be directly called by the user.

