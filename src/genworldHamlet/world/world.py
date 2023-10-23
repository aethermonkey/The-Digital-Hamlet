from genworlds.worlds.concrete.base.world import BaseWorld
from genworlds.agents.concrete.basic_assistant.utils import generate_basic_assistant
from genworlds.worlds.concrete.base.actions import UserSpeaksWithAgentEvent

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = "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"

Hamlet = BaseWorld(
    name="Hamlet",
    description="The world of The Digital Hamlet",
)

description = """Agent that helps the user to answer questions."""

# Generate a basic assistant (you have to provide the openai_api_key)
Librarian = generate_basic_assistant(
    agent_name="Librarian",
    description=description,
    openai_api_key=openai_api_key
)

# Add wakeup events to the agents so you can interact with the agent after is sleeping
Librarian.add_wakeup_event(event_class=UserSpeaksWithAgentEvent)

## Attach the agent to the World
Hamlet.add_agent(Librarian)
print (Hamlet.agents)

Hamlet.launch()