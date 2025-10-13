class IntelTools:
    @staticmethod
    def encrypt_message(msg: str):
        return msg[::-1]  # Simple reversal for demonstration

    @staticmethod
    def log_transmission(agent_name: str, message: str):
        print(f"{agent_name} sent encrypted message: {message}")
