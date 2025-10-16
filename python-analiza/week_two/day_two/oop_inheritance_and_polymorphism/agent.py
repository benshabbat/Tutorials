

class Agent:
    total_agents = 0

    def __init__(self, code_name:str , clearance_level : int = 0):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1
        

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")

    def set_clearance_level(self, new_level: int):
        if new_level < 1 or new_level > 10:
            print("Clearance level must be between 1 and 10.")
        else:
            self._clearance_level = new_level
            print(f"Clearance level updated to {self._clearance_level}")
            
            
    def get_clearance_level(self):
        print(f"Current clearance level: {self._clearance_level}")
        return self._clearance_level
    
    @staticmethod
    def get_total_agents():
        print(f"Total agents created: {Agent.total_agents}")
        return Agent.total_agents




#     @property
#     def clearance_level(self):
#         """Getter for clearance level"""
#         print(f"Current clearance level: {self.__clearance_level}")
#         return self.__clearance_level
    
#     @clearance_level.setter
#     def clearance_level(self, new_level: int):
#         """Setter for clearance level"""
#         if new_level < 1 or new_level > 5:
#             print("Clearance level must be between 1 and 5.")
#         else:
#             self.__clearance_level = new_level
#             print(f"Clearance level updated to {self.__clearance_level}")
    
    
# ag = Agent("Eagle", 3)
# ag.report()

# # עכשיו נוכל לגשת ל-clearance_level כמו משתנה רגיל
# print(f"Getting clearance level: {ag.clearance_level}")  # קורא ל-getter
# ag.clearance_level = 4  # קורא ל-setter
# print(f"After update: {ag.clearance_level}")  # קורא ל-getter שוב
    
    