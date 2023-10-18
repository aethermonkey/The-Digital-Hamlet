from autogen_agent import AutogenAgent
from conversation_models import Message, Conversation
from django.utils import timezone

class LibraryChat:
    def __init__(self, library_agent, other_agent):
        self.library_agent = library_agent
        self.other_agent = other_agent
        self.conversation = Conversation.objects.create(agents=[library_agent, other_agent])
        self.conversation.save()

    def send_message(self, message_content):
        message = Message.objects.create(
            conversation=self.conversation,
            message=message_content,
            created_at=timezone.now()
        )
        message.save()

    def receive_message(self, message_content):
        message = Message.objects.create(
            conversation=self.conversation,
            message=message_content,
            created_at=timezone.now()
        )
        message.save()

    def start_chat(self):
        autogen_agent = AutogenAgent(self.library_agent, self.other_agent)
        autogen_agent.start_conversation()
