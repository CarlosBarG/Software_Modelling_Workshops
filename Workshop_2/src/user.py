"""
    This module contains the class definition from the user from the Arcade-Store.
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

from typing import List
from arcade_machine import ArcadeMachine
from game import Game

class User:
    """
    This class represents a user for the Arcade store
    
    Attributes:
        user_name(Str): It's the name of the user
        user_id(Str): It's the identification of the user
        user_home_address(Str): It's the home_address of the user
        purchased_machines(List): A list of the machines purchased for the user.
        purchased_games(List): A list of the games purchased for the user.
        purchased_merchandising(List): A list of the merchandising purchased for the user.


    """
    def __init__(self, user_name: str, user_id: str, user_home_address: str):
        self.user_name = user_name
        self.user_id = user_id
        self.user_home_address= user_home_address
        self.purchased_machines = []
        self.purchased_games = []
        self.purchased_merchandising = []

    def show_purchased_machines(self):
        """
            Show the details of all arcade machines purchased by the user.
        """
        if self.purchased_machines:
            print("Purchased Machines:")
            for machine in self.purchased_machines:
                machine.show_details()
        else:
            print("No machines purchased yet.")

    def show_purchased_games(self):
        """
            Show the details of all games purchased by the user.
        """
        if self.purchased_games:
            print("Purchased Games:")
            for game in self.purchased_games:
                game.show_game_details()
        else:
            print("No games purchased yet.")
    
    def show_purchased_merchandising(self):
        """
            Show the details of all merchandising items purchased by the user.
        """
        if self.purchased_merchandising:
            print("Purchased Merchandising:")
            for merch in self.purchased_merchandising:
                print(merch)
        else:
            print("No merchandising purchased yet.")
    
    def buy_arcade_machine(self, machine: ArcadeMachine):
        """
        Add an arcade machine to the user list of purchased machines.
        
        Args:
            machine (ArcadeMachine): The arcade machine to be purchased.
        """
        self.purchased_machines.append(machine)

    def buy_game(self, game: Game):
        """
        Add a game to the user list of purchased games.
        
        Args:
            game (Game) : The game to be purchased.
        """
        self.purchased_games.append(game)

    def buy_merchandising(self, merch):
        """
        Add a merchandising item to the user list of purchased merchandising.
        
        Args:
            merch (str): The merchandising item to be purchased.
        """
        self.purchased_merchandising.append(merch)
   



        


    



