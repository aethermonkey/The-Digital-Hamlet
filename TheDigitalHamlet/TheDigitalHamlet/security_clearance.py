from django.db import models
from ..TheDigitalHamlet.base_models import BaseAgent

# Create your models here.

# A class for security clearance of agents (and users)
# Will be a foreign key for agents and users
# Need a simple framework for dictating clearance levels

class SecurityClearance(models.Model):
    
    agent_id = models.ForeignKey(BaseAgent.agent_id, on_delete=models.CASCADE)
    clearance = models.UUIDField()
    
    class meta:
        abstract = True
    
    def get_clearance(agent_id):
        return clearance

