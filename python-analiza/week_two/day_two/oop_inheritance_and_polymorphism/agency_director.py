from field_agent import FieldAgent
from cyber_agent import CyberAgent
from agent import Agent

class AgencyDirector:
    _instance = None

    def __new__(cls,name):
        if cls._instance is None:
            cls._instance = super(AgencyDirector, cls).__new__(cls,name)
            # cls._instance = super().__new__(cls)
            cls._instance.agents = []
            cls._instance.name = name
        return cls._instance

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)   
    def list_agents(self):
        for agent in self.agents:
            agent.report()  
            
    def total_agents(self):
        return len(self.agents)
    def find_agent_by_code_name(self, code_name):
        for agent in self.agents:
            if agent.code_name == code_name:
                return agent
        return None
    def promote_agent(self, code_name, new_clearance_level):
        agent = self.find_agent_by_code_name(code_name)
        if agent:
            agent.set_clearance_level(new_clearance_level)
        else:
            print(f"No agent found with code name: {code_name}")
    def agent_clearance_report(self):
        for agent in self.agents:
            print(f"Agent {agent.code_name}: Clearance Level {agent.get_clearance_level()}")
    def __str__(self):
        return f"AgencyDirector managing {self.total_agents()} agents."
    def __repr__(self):
        return f"<AgencyDirector: {self.total_agents()} agents>"

# Example usage:
director = AgencyDirector()   
agent1 = FieldAgent("Eagle", 5, "Berlin")
agent2 = CyberAgent("Shadow", 7, "Hacking")
director.add_agent(agent1)
director.add_agent(agent2)
director.list_agents()
director.promote_agent("Eagle", 6)
director.agent_clearance_report()
print(director)
print(Agent.get_total_agents())
print(repr(director))
director2 = AgencyDirector()
print(director2)
print(repr(director2))
print(director is director2)  # Should print True, confirming singleton behavior