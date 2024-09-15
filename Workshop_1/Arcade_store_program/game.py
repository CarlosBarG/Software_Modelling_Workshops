"""
    This module contains the class definition from a game from the Arcade_Store.
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

class Game:
    """
    This class represents a game from the Arcade store.

    Attributes:
        name(Str): It's the name of the game
        year_of_release(Str): It's the year of release of the game
        price(Str): It's the price of the game
        
    """
    def __init__(self, name: str, year_of_release: str, price: str):
        self.name = name
        self.year_of_release = year_of_release
        self.price = price

    def show_game_details(self):
        """
        Show the attributes of the game, including the name, year of release, and price.
        """
        
        print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}")