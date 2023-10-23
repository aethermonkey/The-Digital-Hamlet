from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import auth
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from autogen.agentchat.assistant_agent import AssistantAgent
from autogen.agentchat.user_proxy_agent import UserProxyAgent
# from autogen.agentchat
from typing import Callable, Dict, Optional, Union

DEFAULT_SYSTEM_MESSAGE = """You are a helpful AI assistant.
Solve tasks using your coding and language skills.
"""

       

class GeoEntity(models.Model):
    object_id = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=200)
    coords = models.JSONField("Spatial Coordinates", "coords", default=list)


    class Meta:
        abstract = True

# class BaseConfigList(models.Model):

class BaseAgent(AssistantAgent, models.Model):
    def __init__(
        self,
        name: str,
        system_message: Optional[str] = DEFAULT_SYSTEM_MESSAGE,
        llm_config: Optional[Union[Dict, bool]] = None,
        is_termination_msg: Optional[Callable[[Dict], bool]] = None,
        max_consecutive_auto_reply: Optional[int] = None,
        human_input_mode: Optional[str] = "NEVER",
        code_execution_config: Optional[Union[Dict, bool]] = False,
        **kwargs,
    ):
        """
        Args:
            name (str): agent name.
            system_message (str): system message for the ChatCompletion inference.
                Please override this attribute if you want to reprogram the agent.
            llm_config (dict): llm inference configuration.
                Please refer to [Completion.create](/docs/reference/oai/completion#create)
                for available options.
            is_termination_msg (function): a function that takes a message in the form of a dictionary
                and returns a boolean value indicating if this received message is a termination message.
                The dict can contain the following keys: "content", "role", "name", "function_call".
            max_consecutive_auto_reply (int): the maximum number of consecutive auto replies.
                default to None (no limit provided, class attribute MAX_CONSECUTIVE_AUTO_REPLY will be used as the limit in this case).
                The limit only plays a role when human_input_mode is not "ALWAYS".
            **kwargs (dict): Please refer to other kwargs in
                [ConversableAgent](conversable_agent#__init__).
        """
        super().__init__(
            name,
            system_message,
            is_termination_msg,
            max_consecutive_auto_reply,
            human_input_mode,
            code_execution_config,
            llm_config,
            **kwargs,
            
        )
    agent_id = models.UUIDField(primary_key=True)
    age = models.PositiveIntegerField()
    # traits = models.JSONField(default=dict)
    clearance = models.JSONField(default=dict)
    bank_balance = models.FloatField(default=0.0,)

    class Meta:
        abstract = True

class BaseUserProxyAgent (UserProxyAgent, models.Model):
    def __init__(self, name, code_execution_config):
        super().__init__(name, code_execution_config)
    agent_id = models.UUIDField(primary_key=True)
    dob = models.PositiveIntegerField()
    clearance = models.JSONField(default=dict)
    bank_balance = models.FloatField(default=0.0,)

class BaseBuilding(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseService(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(BaseAgent, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseEvent(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)
    time = models.DateTimeField()
    participants = models.ManyToManyField(BaseAgent)

    class Meta:
        abstract = True

class BaseItem(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(BaseAgent, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)

    class Meta:
        abstract = True

class BaseCurrency(models.Model):
    name = models.CharField(max_length=200)
    currency_code = models.CharField(max_length=8)
    location = models.ForeignKey(GeoEntity, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    # The BaseCurrency represents currencies within the digital hamlet.
    # We will likely need to work out some exchange system in future for realizing exchange rates
    # between hamlet currency and outside world currency, like USD, AUD, cryptos, etc.
