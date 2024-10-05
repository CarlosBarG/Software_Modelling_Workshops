
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

    store = Store()
    
  


    MENU = """
    1.  Buy a arcade machine
    2. Buy a game from the arcade machine
    3. Buy merchandising
    4. Show the purchased machines
    5. Show the purchased games
    6. Show the purchased merchandising
    0. Exit
    """
    

    MENU_BUY_ARCADE = """
    1. Show available arcade machines by price range
    2. Show available arcade machines by material
    3. Show available arcade machines by weight range
    4. Show available arcade machines by power consumption range
    5. Show available arcade machines by number of games




    """
    option = None
    while option != "0":
        option = input(MENU).strip()

        if option == "1":
            print(MENU_BUY_ARCADE)
            option_buy_arcade = input().strip()
            if option_buy_arcade == "1":
                price_range = input("Enter the price range (min-max): ").strip()
                store.show_machines_by_price_range(price_range)
            elif option_buy_arcade == "2":
                material = input("Enter the material: ").strip()
                store.show_machines_by_material(material)
            elif option_buy_arcade == "3":
                weight_range = input("Enter the weight range (min-max): ").strip()
                store.show_machines_by_weight_range(weight_range)
            elif option_buy_arcade == "4":
                power_consumption_range = input("Enter the power consumption range (min-max): ").strip()
                store.show_machines_by_power_consumption_range(power_consumption_range)
            elif option_buy_arcade == "5":
                number_of_games = input("Enter the number of games: ").strip()
                store.show_machines_by_number_of_games(number_of_games)
            else:
                print("Invalid option")
        elif option == "2":
            game_code = input("Enter the game code: ")
            game.machine.add_game(game_code)
        elif option == "3":
            store.show_merchandising()
            merch = input("Enter the merchandising item: ")
            store.buy_merchandising(merch)
        elif option == "4":
            user.show_purchased_machines()
        elif option == "5":
            user.show_purchased_games()
        elif option == "6":
            user.show_purchased_merchandising()

if __name__ == "__main__":
    main()