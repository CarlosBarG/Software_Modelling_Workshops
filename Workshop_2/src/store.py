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
    
    def show_machines_by_price_range(self, min_price: float, max_price: float):
        """
        Show all arcade machines available in the store within a price range.

        Args:
            min_price (float): The minimum price of the arcade machines to display.
            max_price (float): The maximum price of the arcade machines to display.
        """
        machines_in_range = [machine for machine in self.available_arcades_machines if min_price <= machine.price <= max_price]
        
        if machines_in_range:
            print(f"Arcade Machines in Store between ${min_price} and ${max_price}:")
            for machine in machines_in_range:
                machine.show_details()
        else:
            print(f"No arcade machines available in the store between ${min_price} and ${max_price}.")
    
    def show_machines_by_weight_range(self, min_weight: float, max_weight: float):
        """
        Show all arcade machines available in the store within a weight range.

        Args:
            min_weight (float): The minimum weight of the arcade machines to display.
            max_weight (float): The maximum weight of the arcade machines to display.
        """
        machines_in_range = [machine for machine in self.available_arcades_machines if min_weight <= machine.machine_weight <= max_weight]
        
        if machines_in_range:
            print(f"Arcade Machines in Store between {min_weight} and {max_weight} kg:")
            for machine in machines_in_range:
                machine.show_details()
        else:
            print(f"No arcade machines available in the store between {min_weight} and {max_weight} kg.")

    def show_machines_by_power_consumption_range(self, min_power_consumption: float, max_power_consumption: float):
        """
        Show all arcade machines available in the store within a power consumption range.

        Args:
            min_power_consumption (float): The minimum power consumption of the arcade machines to display.
            max_power_consumption (float): The maximum power consumption of the arcade machines to display.
        """
        machines_in_range = [machine for machine in self.available_arcades_machines if min_power_consumption <= machine.power_consumption <= max_power_consumption]
        
        if machines_in_range:
            print(f"Arcade Machines in Store between {min_power_consumption} and {max_power_consumption} W:")
            for machine in machines_in_range:
                machine.show_details()
        else:
            print(f"No arcade machines available in the store between {min_power_consumption} and {max_power_consumption} W.")

        
    def show_machines_by_material(self, material: str):
        """
        Show all arcade machines available in the store with a specific material.

        Args:
            material (str): The material of the arcade machines to display.
        """
        machines_by_material = [machine for machine in self.available_arcades_machines if machine.machine_material == material]
        
        if machines_by_material:
            print(f"Arcade Machines in Store with material {material}:")
            for machine in machines_by_material:
                machine.show_details()
        else:
            print(f"No arcade machines available in the store with material {material}.")
    def show_machines_by_games_quantity(self, min_games: int, max_games: int):
        """
        Show all arcade machines available in the store with a specific number of games.

        Args:
            min_games (int): The minimum number of games of the arcade machines to display.
            max_games (int): The maximum number of games of the arcade machines to display.
        """
        machines_by_games = [machine for machine in self.available_arcades_machines if min_games <= len(machine.games) <= max_games]
        
        if machines_by_games:
            print(f"Arcade Machines in Store with {min_games} to {max_games} games:")
            for machine in machines_by_games:
                machine.show_details()
        else:
            print(f"No arcade machines available in the store with {min_games} to {max_games} games.")

    
        

    def add_arcade_machine(self, arcade_machine):

        """
        Add an arcade machine to the store's inventory.

        Args:
            arcade_machine (ArcadeMachine): The arcade machine to add to the store.
        """
        FactoryArcadeMachine = ArcadeMachine(arcade_machine)
        self.available_arcades_machines.append(FactoryArcadeMachine)



    def add_merchandising(self, item):
        """
        Add a merchandising item to the store's inventory.

        Args:
            item (str): The merchandising item to add to the store.
        """
        self.available_merchandising.append(item)

   