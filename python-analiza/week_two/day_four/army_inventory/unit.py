from soldier import Soldier

class Unit:
    def __init__(self, unit_name:str, commander:Soldier, soldiers:list[Soldier]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers

    def briefing(self):
        briefing_str = f"Unit: {self.unit_name}\nCommander: {self.commander.report()}\nSoldiers:\n"
        # for soldier in self.soldiers:
        #     briefing_str += f" - {soldier.report()}\n"
        return briefing_str
    
