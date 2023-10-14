# groupchat.py Cheat Sheet

## Module Information

- **Module**: groupchat.py
- **Path**: /plan/autogen/agentchat/groupchat.py

## Description

The `groupchat.py` module provides a class `GroupChat` that represents a group chat with multiple agents. It also includes a class `GroupChatManager` that serves as a chat manager agent for managing the group chat.

## Class

### GroupChat

- **Description**: A class that represents a group chat with multiple agents.
- **Data Attributes**:
  - `agents` (List[Agent]): The list of agents participating in the group chat.
  - `messages` (List[Dict]): The list of messages exchanged in the group chat.
  - `max_round` (int): The maximum number of rounds in the group chat.
  - `admin_name` (str): The name of the admin agent in the group chat.

#### Properties

- `agent_names`: Returns the names of the agents in the group chat.

#### Methods

- `reset()`: Resets the group chat.
- `agent_by_name(name: str) -> Agent`: Finds an agent in the group chat by name.
- `next_agent(agent: Agent) -> Agent`: Returns the next agent in the group chat.
- `select_speaker_msg() -> str`: Returns the message for selecting the next speaker.
- `select_speaker(last_speaker: Agent, selector: ConversableAgent) -> Agent`: Selects the next speaker.
- `_participant_roles() -> str`: Returns the roles of the participants in the group chat.

### GroupChatManager

- **Description**: A class that serves as a chat manager agent for managing a group chat.
- **Inherits**: ConversableAgent

#### Methods

- `__init__(groupchat: GroupChat, name: Optional[str] = "chat_manager", max_consecutive_auto_reply: Optional[int] = sys.maxsize, human_input_mode: Optional[str] = "NEVER", system_message: Optional[str] = "Group chat manager.", **kwargs)`: Initializes the GroupChatManager object.
- `run_chat(messages: Optional[List[Dict]] = None, sender: Optional[Agent] = None, config: Optional[GroupChat] = None) -> Union[str, Dict, None]`: Runs the group chat.
