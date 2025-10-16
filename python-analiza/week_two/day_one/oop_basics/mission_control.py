from report import Report

class MissionControl:  
    
    
    def analyze_report(self, r: Report):
        if r.urgency_level >= 4:
            print("Immediate response required.")
        elif r.urgency_level == 3:
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis.")
