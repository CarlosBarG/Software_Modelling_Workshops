"""
    This module contains the class definition from the store.
    This file is part of the Arcade-store
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
from game import Game
from arcade_machine import ArcadeMachine

class Store:
    """
        This class represents a store that have arcade machines, games, and merchandising.

        Attributes:
            available_arcades_machines (List): A list of arcade machines available in the store.
            available_merchandising (List): A list of merchandising items available in the store.
    """
    def __init__(self):
        self.available_arcades_machines = []
        self.available_merchandising = []

    def show_arcade_machines(self):
        """

        Show the details of all arcade machines available in the store.
        
        """
        
        if self.available_arcades_machines:
            print("Arcade Machines in Store:")
            for machine in self.available_arcades_machines:
                machine.show_details()
        else:
            print("No arcade machines available in the store.")

    def show_merchandising(self):
        """
            Show all merchandising items available in the store.
            
        """
        if self.available_merchandising:
            print("Merchandising in Store:")
            for item in self.available_merchandising:
                print(item)
        else:
            print("No merchandising available in the store.")

    def show_games(self):
         
        """
         Displays all games available in the store.   
        """
        games = []
        for machine in self.available_arcades_machines:
            for game in machine.games:
                games.append(game)
        
        if games:
            print("Games in Store:")
            for game in games:
                game.show_game_details()
        else:
            print("No games available in the store.")

    def add_arcade_machine(self, arcade_machine: ArcadeMachine):

        """
        Add an arcade machine to the store's inventory.

        Args:
            arcade_machine (ArcadeMachine): The arcade machine to add to the store.
        """
        self.available_arcades_machines.append(arcade_machine)

    def add_merchandising(self, item):
        """
        Add a merchandising item to the store's inventory.

        Args:
            item (str): The merchandising item to add to the store.
        """
        self.available_merchandising.append(item)

    def purchase_item(self, user, item_type, item):
        """
         Add the purchased item to the user's list of purchased items.

        Args:
            user: The user making the purchase.
            item_type (str): The type of item being purchased. Can be "arcade_machine", "game", or "merchandising".
            item: The item being purchased.
        """
        if item_type == "arcade_machine":
            user.buy_arcade_machine(item)
        elif item_type == "game":
            user.buy_game(item)
        elif item_type == "merchandising":
            user.buy_merchandising(item)