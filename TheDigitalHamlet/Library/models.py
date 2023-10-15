from TheDigitalHamlet.TheDigitalHamlet.base_models import BaseAgent
from django.utils import timezone

class LibraryAgent(BaseAgent):
    def __init__(self, name, age, location, traits):
        super().__init__(name, age, location, traits)

    def daily_conversations_summary(self, query):
        # Get the current date
        current_date = timezone.now().date()

        # Filter conversations for the current day
        conversations = Conversation.objects.filter(created_at__date=current_date, message__icontains=query)

        # Create a summary of daily conversations
        summary = ""
        for conversation in conversations:
            summary += f"Conversation between {', '.join(str(agent) for agent in conversation.agents)}\n"
            summary += f"Message: {conversation.message}\n"
            summary += "------------------------\n"

        # Store the summary as knowledge
        self.store_knowledge(summary)

    # ... rest of the code ...
