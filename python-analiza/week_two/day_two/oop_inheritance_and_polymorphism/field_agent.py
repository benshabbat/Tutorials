from agent import Agent

class FieldAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, region: str):
        super().__init__(code_name, clearance_level)
        self.region = region
    def report(self):
        super().report()
        print(f"Region: {self.region}")
        

        # print(f"Field Agent {self.code_name} reporting from {self.region}. Clearance Level: {self._clearance_level}")