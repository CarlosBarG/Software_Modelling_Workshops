"""
    This module contains the class definition from the arcade machine.
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
from game import Game

class ArcadeMachine:
    """
    This class represents an arcade machine of the Arcade store.

    Attributes:
        machine_name (str): The name of the arcade machine.
        machine_material (str): The material of the arcade machine.
        creation_year (str): The year of creation of the arcade. 
        price (str): The price of the arcade machine.
        games (List[Game]): A list of games available on this arcade machine.
    """
    def __init__(self, machine_name: str, machine_material: str, creation_year: str, price: str):
        self.machine_name = machine_name
        self.machine_material = machine_material
        self.creation_year = creation_year
        self.price = price
        self.games = []

    def add_game(self, game: Game):
        """
        Add a game to the arcade machine.

        Args:
            game (Game): The game to add to the arcade machine.
        """
        self.games.append(game)

    def show_details(self):
        """
        Show the details of the arcade machine, including its name, creation year, and price.
        """
        print(f"Arcade Machine: {self.machine_name}, Creation Year: {self.creation_year}, Price: ${self.price}")
        