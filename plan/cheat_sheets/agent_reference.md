# Agent Class

The `Agent` class is an abstract class for AI agents.

## Constructor

- `__init__(self, name: str)`: Initializes the agent with a name.

## Properties

- `name`: Returns the name of the agent.

## Methods

- `send(self, message: Union[Dict, str], recipient: Agent, request_reply: Optional[bool] = None)`: Sends a message to another agent.
- `receive(self, message: Union[Dict, str], sender: Agent, request_reply: Optional[bool] = None)`: Receives a message from another agent.
- `reset(self)`: Resets the agent.
- `generate_reply(self, messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, **kwargs) -> Union[str, Dict, None]`: Generates a reply based on the received messages.

