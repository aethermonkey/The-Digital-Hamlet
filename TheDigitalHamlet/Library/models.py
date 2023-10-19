from django.db import models
from ..base_models import BaseAgent
from django.utils import timezone
from .storage_models import Conversation
from .storage_models import Knowledge
from TheDigitalHamlet.TheDigitalHamlet.models import GeoEntity
from .nlp_tools import sum_up


class Library(GeoEntity):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    database = models.JSONField()

    def create_data_sql(self, data):
        # db.create_data_sql(data)
        pass

    def read_data_sql(self, data_id):
        # db.read_data_sql(data_id)
        pass

    def update_data_sql(self, data_id, new_data):
        # db.update_data_sql(data_id, new_data)
        pass

    def delete_data_sql(self, data_id):
        # db.delete_data_sql(data_id)
        pass

class LibraryAgent(BaseAgent):
    def __init__(self, name, llm_config):
        super().__init__(name, llm_config)

    def send_message(self, message_content):
        self.send_message(message_content)

    def receive_message(self, message_content):
        self.receive_message(message_content)

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

        # Use the function from nlp_tools.py to create a summary
        summary = sum_up(join_conversations, "Azma-AI/bart-conversation-summarizer", do_sample=True)
        return summary

    def store_knowledge(self, title, content, medium, classification):
        # Store the knowledge in a structured format
        knowledge_entry = Knowledge.objects.create(title, content, medium, classification)
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
    def __init__(self, name, age, traits):
        super().__init__(name, age, traits)
