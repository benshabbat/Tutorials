from agent import Agent

class CyberAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, specialty: str):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        super().report()
        print(f"Specialty: {self.specialty}")
        
