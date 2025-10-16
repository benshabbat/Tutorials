
from agent import Agent


class Mission:
    def __init__(self, mission_name: str, target_location : str, assigned_agent : Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
    
    def brief(self):
        print(f"Mission: {self.mission_name}, Target: {self.target_location} ,Agent: {self.assigned_agent.code_name}")
 


mission1 = Mission("Operation Silent Night", "Berlin", Agent("Shadow", 5))

mission1.brief()