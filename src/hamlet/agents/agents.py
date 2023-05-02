class Agent:
    """Abstract parent class for all agents"""
    def __init__(self, name, agent_id, location): 
        self.name = name  
        self.agent_id = agent_id 
        self.location = location 
        self.traits = {} # Dict of character traits and levels 

class ResidentAgent(Agent):
    """Generic resident agent within the hamlet"""
    def __init__(self, name, agent_id, location):
        super().__init__(name, agent_id, location)
        self.role = None  # Job or purpose 
        self.skills = [] # List of abilities 
        self.relationships = [] # Network of other agents interacted with
        self.balance = 0 # Economic currency balance
        
class InfrastructureAgent(Agent):
    """Parent class for infrastructure role agents""" 
    def __init__(self, name, agent_id, location): 
        super().__init__(name, agent_id, location)
        self.duties = [] # Responsibilities in administering the hamlet
        
class SovereignAgent(Agent):  
    """Serves the sovereign directly"""
    def __init__(self, name, agent_id, location): 
        super().__init__(name, agent_id, location)
        self.loyalty = 10 # Level of dedication to the sovereign
        self.security_level = 5 # Level of access to sovereign data 
        
class LegalAgent(InfrastructureAgent): 
    """Upholds VeritasSuprema constitution and enforces law"""
    def __init__(self, name, agent_id, location):
        super().__init__(name, agent_id, location)
        self.standards = [] # List of laws and rules to enforce