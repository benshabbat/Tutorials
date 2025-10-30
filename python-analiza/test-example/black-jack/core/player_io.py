def ask_player_action() -> str:
    req =  input("Do you want stands press S or to get more card press H: ")
    while req != "S" and req != "H":
        req =  input("Do you want stands press S or to get more card press H: ")
        
    return req


  
        
        