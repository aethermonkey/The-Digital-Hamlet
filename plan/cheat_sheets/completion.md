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

