from agent import Agent

class IntelTools:
    @staticmethod
    def encrypt_message(msg: str):
        return msg[::-1]  # Simple reversal for demonstration

    @staticmethod
    def log_transmission(agent: Agent, message: str):
        print(f"{agent.code_name} sent encrypted message: {message}")
