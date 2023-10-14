# MathUserProxyAgent Class

The `MathUserProxyAgent` class is a subclass of `UserProxyAgent` and is designed to handle math problems.

## Constructor

- `__init__(self, name: Optional[str] = "MathChatAgent", is_termination_msg: Optional[Callable[[Dict], bool]] = _is_termination_msg_mathchat, human_input_mode: Optional[str] = "NEVER", default_auto_reply: Optional[Union[str, Dict, None]] = DEFAULT_REPLY, max_invalid_q_per_step: int = 3, **kwargs)`: Initializes the `MathUserProxyAgent` with the provided parameters.

## Methods

- `_is_termination_msg_mathchat(message)`: Checks if a message is a termination message.
- `_add_print_to_last_line(code)`: Adds `print()` to the last line of a string.
- `_remove_print(code)`: Removes all `print` statements from a string.
- `generate_init_message(self, problem, prompt_type="default", customized_prompt=None)`: Generates a prompt for the assistant agent with the given problem and prompt.
- `_generate_math_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, config: Optional[Any] = None)`: Generates an auto reply for math problems.

