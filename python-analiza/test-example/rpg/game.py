import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc
from core.boss import Boss

class Game:
    def start(self):
        self.show_menu()
        
    def create_player(self):
        player_name = input("Enter your player's name: ")
        player = Player(name=player_name)
        print(f"Player {player.name} created with profession {player.profession}.")
        return player
        
    def show_menu(self):
        
        menu = """
        Welcome to the RPG Game!
        1. Start Battle
        2. Maze Challenge
        3. Exit Game
        """
        res = input(menu)
        while res not in ["1","2","3"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            res = input(menu)
        if res == "1":
            player = self.create_player()
            monster = self.choose_random_monster()
            self.battle(player, monster)
        elif res == "2":
            self.maze()    
        elif res == "3":
            self.exit_game()
        return res

    def choose_random_monster(self):
        monsters = ["Goblin", "Orc"]
        monster = random.choice(monsters)
        if monster == "Goblin":
            return Goblin()
        elif monster == "Orc":
            return Orc()

    def battle(self, player, monster):
        player.roll = self.roll_dice(6) + player.speed
        monster.roll = self.roll_dice(6) + monster.speed
        print(f"{player.name} rolls {player.roll} plus speed {player.speed} = {player.roll}")
        print(f"{monster.name} rolls {monster.roll} plus speed {monster.speed} = {monster.roll}")
        if player.roll >= monster.roll:
            player.turn = True
            print(f"{player.name} starts the battle against {monster.name}!")
        else:
            monster.turn = True
            print(f"{monster.name} starts the battle against {player.name}!")

        while player.hp > 0 and monster.hp > 0:
            if player.turn:
                player.roll = self.roll_dice(20) + player.speed
                print(f"{player.name} rolls {player.roll} plus speed {player.speed} = {player.roll}")
                if player.roll > monster.armor_rating:
                    player.attack(monster)
                else:
                    print(f"{player.name} missed the attack!")
                player.turn = False
                monster.turn = True
            else:
                monster.roll = self.roll_dice(20) + monster.speed
                print(f"{monster.name} rolls {monster.roll} plus speed {monster.speed} = {monster.roll}")
                if monster.type == "goblin" and monster.hp>10:
                    list_run_away = [1,1,1,0,0,0,0,0,0,0]
                    random.shuffle(list_run_away)
                    roll_run_away = random.randint(0,9)
                    if list_run_away[roll_run_away]==1:
                        monster.run_away()
                        break

                if monster.roll > player.armor_rating:
                    monster.attack(player)
                else:
                    print(f"{monster.name} missed the attack!")
                monster.turn = False
                player.turn = True
        if player.hp <= 0:
            print(f"{player.name} has been defeated by {monster.name}!")
        elif monster.run_away():
            print(f"{monster.name} has run away from {player.name}!")  
        else:
            print(f"{player.name} has defeated {monster.name}!")

    def roll_dice(self, sides):
        return random.randint(1, sides)
    
    def exit_game(self):
        print("Exiting game. Goodbye!")
        exit()
        
        
        
    def maze(self):
        rooms = [None for _ in range(8)]
        for i in range(len(rooms)):
            if rooms[i] is None:
                rooms[i] = self.choose_random_monster()
                
        player = self.create_player()
        for i in range(len(rooms)):
            self.battle(player, rooms[i])
            if rooms[i].hp <= 0:
                print(f"Room {i+1}: You have defeated the monster!")
            else:
                print(f"Room {i+1}: You fled from the monster!")
                break
        if player.hp > 0:    
            print("Congratulations! You have completed the maze challenge.")
            print("Final Battle with the Boss!")  
            boss = Boss()  
            self.battle(player, boss)
            if player.hp <= 0:
                print(f"{player.name} has been defeated by {boss.name}!")
            elif boss.hp <= 0:
                print(f"{boss.name} has been defeated by {player.name}!")
                print("You WON the RPG Game!")
                print("Thank you for playing!")
