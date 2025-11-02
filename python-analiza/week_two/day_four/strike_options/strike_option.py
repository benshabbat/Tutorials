class StrikeOption:
    def __init__(self, name:str,ammo:int):
        self.name = name
        self.ammo = ammo
        
    def payoff(self, underlying_price):
        if self.option_type == 'call':
            return max(0, underlying_price - self.strike_price)
        elif self.option_type == 'put':
            return max(0, self.strike_price - underlying_price)
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")