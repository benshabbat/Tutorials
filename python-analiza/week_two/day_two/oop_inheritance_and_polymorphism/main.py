from agent import Agent
from field_agent import FieldAgent
from cyber_agent import CyberAgent


ag = Agent("Eagle", 3)
ag2 = Agent("Hawk", 7)
agf = FieldAgent("Fox", 6, "Europe")
agc = CyberAgent("Netrunner", 8, "Hacking")
agent_list = [ag, ag2, agf, agc]


def list_agents(agents):
    print("Listing all agents:")
    for agent in agents:
        agent.report()
    
if __name__ == "__main__":
    list_agents(agent_list)