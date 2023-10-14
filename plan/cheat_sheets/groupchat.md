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
