from TheDigitalHamlet.TheDigitalHamlet.base_models import BaseAgent
from TheDigitalHamlet.Library.conversation_models import Conversation
from TheDigitalHamlet.Library.knowledge_models import Knowledge
from datetime import timezone

class LibraryAgent(BaseAgent):
    def __init__(self, name, age, location, traits):
        super().__init__(name, age, location, traits)

    def daily_conversations_summary(self):
        # Get the current date
        current_date = timezone.now().date()

        # Filter conversations for the current day
        conversations = Conversation.objects.filter(created_at__date=current_date)

        # Create a summary of daily conversations
        join_conversations = ""
        for conversation in conversations:
            join_conversations += f"Conversation between {', '.join(str(agent) for agent in conversation.agents)}\n"
            join_conversations += f"Created: {conversation.created_at}\n"
            join_conversations += f"Message: {conversation.message}\n"
            join_conversations += "------------------------\n"

        summary = ""
        # use a NLP library to chunck the join_conversations and summarise them into one single output summary of about 500 words
        # TODO: use a NLP library
        summary += join_conversations
        

        # Store the summary as knowledge
        self.store_knowledge(summary)

    def store_knowledge(self, knowledge):
        # Store the knowledge in a structured format
        knowledge_entry = Knowledge.objects.create(title="Daily Conversations Summary", content=knowledge, medium="Text", classification="Summary")
        knowledge_entry.save()

    def search_knowledge(self, query):
        # Search the knowledge system for information based on the query
        knowledge_entries = Knowledge.objects.filter(content__icontains=query)
        return knowledge_entries

    def advise_municipal_agents(self):
        # Advise the municipal agents on high-level descriptions of how the Library can achieve a knowledge system fit for Artificial General Intelligence
        pass

    def liaise_with_agents(self, agents):
        # Liaise with other agents to provide information from the knowledge system
        pass

    def check_authorisation(self, agent):
        # Check the authorisation level of an agent to control access to information
        pass

class LibraryManager(BaseAgent):
    def __init__(self, name, age, location, traits):
        super().__init__(name, age, location, traits)
