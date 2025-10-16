from agent import Agent
from Inteltools import IntelTools

from mission_control import MissionControl
from report import Report

if __name__ == "__main__":
    agent = Agent("Unit 8200")
    
    report = Report("msg", 4, agent)

    mission_control = MissionControl()
    mission_control.analyze_report(report)
    
    IntelTools.log_transmission(agent, IntelTools.encrypt_message("Top Secret Message"))