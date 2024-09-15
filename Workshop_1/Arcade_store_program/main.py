
"""
    This module contains the implementation from the Arcade_Store.
    This file is part of the Arcade store
    Author: Carlos Alberto Barriga Gamez

    Arcade-Store is free software: you can redistribute it and/or 
    modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of 
    the License, or (at your option) any later version.

    Arcade-Store is distributed in the hope that it will be useful, 
    but WITHOUT ANY WARRANTY; without even the implied warranty of 
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
    General Public License for more details.

    You should have received a copy of the GNU General Public License 
    along with Arcade-Store. If not, see <https://www.gnu.org/licenses/>. 
"""
from arcade_machine import ArcadeMachine
from game import Game
from store import Store
from user import User

def main():
    """
    Function that runs the Arcade Store program.

    
    This function goes into a loop displaying a menu and allowing users to interact with:
    - View available arcade machines
    - View available games
    - View available merchandising
    - Purchase arcade machines, games, or merchandising
    - View purchased items (arcade machines, games, or merchandising)
    - Exit the program

    The user is prompted for input to select options and provide personal information for purchases.
    """
    store = Store()
    
    
    
    machine1 = ArcadeMachine("Nintendo arcade machine", None, "1980", "300")
    machine2 = ArcadeMachine("Nitro arcade machine", None, "1998", "460")
    
    game1 = Game("Pac-Man", "1980", "50")
    game2 = Game("Tetris", "1984", "60")
    game3 = Game("Super mario bros", "1985", "62")


    machine1.add_game(game1)
    machine1.add_game(game2)
    machine1.add_game(game3)

  

    store.add_arcade_machine(machine1)
    store.add_arcade_machine(machine2)
    merch1= "Pac man T-Shirt - $20"
    merch2= "Snake Cup - $15"
    store.add_merchandising( merch1)
    store.add_merchandising( merch2)


    MENU = """
    1. View arcade machines available
    2. View games available
    3. View merchandising
    4. Purchase Arcade Machine
    5. Purchase game
    6. Purchase merchandising
    7. View purchased Machines
    8. View purchased games
    9. View purchased merchandising
    0. Exit
    """
    
    option = None
    while option != "0":
        option = input(MENU).strip()

        if option == "1":
            store.show_arcade_machines()
        elif option == "2":
            store.show_games()
        elif option == "3":
            store.show_merchandising()
        elif option == "4":
            print("Available Arcade Machines:")
            print (f"1. {machine1.machine_name}")
            print (f"2. {machine2.machine_name}")

                
            machine_number = int(input("Enter the number of the arcade machine to purchase: "))
            if 1 <= machine_number <= len(store.available_arcades_machines):
                selected_machine = store.available_arcades_machines[machine_number - 1]
                print("Select the material for the arcade machine (wood, aluminum, carbon fiber):")
                material = input()
                if material in ["wood", "aluminum", "carbon fiber"]:
                    selected_machine.machine_material = material
                    user = User(None, None, None)
                    user.user_name = input("Enter your name: ")
                    user.user_id = input("Enter your identification number: ")
                    user.user_home_address= input("Enter your home address: ")
                    user.buy_arcade_machine(selected_machine)
                    print(f"The user: {user.user_name} purchased Arcade Machine: {selected_machine.machine_name} with material {selected_machine.machine_material}")
                else:
                    print("Invalid material. Purchase cancelled.")
            else:
                print("Invalid arcade machine number.")
                
        elif option == "5":
            print("Available Games:")
            all_games = []
            
            
            game_number = 1
            for machine in store.available_arcades_machines:
                for game in machine.games:
                    print(f"{game_number}. {game.name}")
                    all_games.append(game)
                    game_number += 1

            if all_games:
                
                game_number = int(input("Enter the number of the game to purchase: "))
                
                if 1 <= game_number <= len(all_games):
                    selected_game = all_games[game_number - 1]
                    user.buy_game(selected_game)
                    print(f"Purchased game: {selected_game.name}")
                else:
                    print("Invalid game number.")
            else:
                print("No games available in the store.")
                
        elif option == "6":
            
            print("Available Merchandising:")
            print (f"1. {merch1}")
            print (f"2. {merch2}")
            merch_number = int(input("Enter the number of the merchandising item to purchase: "))
            if 1 <= merch_number <= len(store.available_merchandising):
                selected_merch = store.available_merchandising[merch_number - 1]
                user.buy_merchandising(selected_merch)
                print(f"Purchased merchandising: {selected_merch}")
            else:
                print("Invalid merchandising number.")
                
        elif option == "7":
            print("Purchased Arcade Machines:")
            if user.purchased_machines:
                for machine in user.purchased_machines:
                    print(f"{machine.machine_name} (Material: {machine.machine_material}, Price: ${machine.price})")
            else:
                print("No arcade machines purchased.")
                
        elif option == "8":
            print("Purchased Games:")
            if user.purchased_games:
                for game in user.purchased_games:
                    print(f"{game.name} (Year: {game.year_of_release}, Price: ${game.price})")
            else:
                print("No games purchased.")
                
        elif option == "9":
            print("Purchased Merchandising:")
            if user.purchased_merchandising:
                for merch in user.purchased_merchandising:
                    print(merch)
            else:
                print("No merchandising purchased.")
                
        elif option == "0":
            print("Closing the program")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()