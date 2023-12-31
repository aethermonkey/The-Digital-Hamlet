from TheDigitalHamlet.TheDigitalHamlet.models import BaseAgent
from .comms.models import Message, Conversation
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
        base_agent = BaseAgent(self.library_agent, self.other_agent)
        base_agent.start_conversation()
