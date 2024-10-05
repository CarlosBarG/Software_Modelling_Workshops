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

        code (int): The code of the game
        name (str): It's the name of the game
        year_of_release (str): It's the year of release of the game
        base_price (float): It's the price of the game
        story_telling_creator (str): It's the creator of the story telling
        graphics_creator (str): It's the creator of the graphics
        category (str): It's the category of the game
        is_hd (bool): It's a boolean that indicates if the game is HD or not
        
        
    """
    def __init__(self,code:int,  name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category:str, is_hd :bool= False):

        self.code = code
        self.name = name
        self.year_of_release = year_of_release
        self.base_price = base_price
        self.story_telling_creator= story_telling_creator
        self.graphics_creator= graphics_creator
        self.category= category
        self.is_hd = is_hd

    def get_code(self):
        return self.code

    

    def get_price(self):

        if self.is_hd:
            self.base_price = self.base_price * 0.1
            return self.base_price
        return self.base_price

    def show_game_details(self):
        """
        Show the attributes of the game, including the name, year of release, and price.
        """
        
        print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.base_price}")
    

class DanceRevolutionGame(Game):
    """
    This class represents a Dance Revolution game from the Arcade store."""

    def __init__(self, code:int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category:str, difficulty: str, number_of_players: int):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd = True)
        
        self.difficulty = difficulty
        self.number_of_players = number_of_players

        def show_game_details(self):
            """
            Show the attributes of the Dance Revolution game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")

class DancingStageGame (Game):
    """
    This class represents a Dancing Stage game from the Arcade store.
    """
    def __init__(self, code:int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category:str, difficulty: str, number_of_players: int):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd = False)
        
        self.difficulty = difficulty
        self.number_of_players = number_of_players

        def show_game_details(self):        
            """
            Show the attributes of the Dancing Stage game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")

class SnakeGame(Game):
    """
    This class represents a Snake game from the Arcade store."""
    def __init__(self, code:int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category:str, difficulty: str, number_of_players: int):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd = False)
        
        self.difficulty = difficulty
        self.number_of_players = number_of_players
        def show_game_details(self):
            """
            Show the attributes of the Snake game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")

class TetrisEffectGame(Game):
    """
    This class represents a Tetris Effect game from the Arcade store."""
    def __init__(self, code: int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category: str,difficulty:str,  number_of_players: int):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd=False)
        self.difficulty = difficulty
        self.number_of_players = number_of_players
        def show_game_details(self):
            """
            Show the attributes of the Tetris Effect game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")
    
class NeedForSpeedGame(Game):
    """
    This class represents a Need For Speed game from the Arcade store."""
    def __init__(self, code: int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category: str,difficulty:str,  number_of_players: int, is_hd= False):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd= True)
        self.difficulty = difficulty
        self.number_of_players = number_of_players
        def show_game_details(self):
            """
            Show the attributes of the Tetris Effect game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")
        
class GhostSquadGame(Game):
    """
    This class represents a Ghost Squad game from the Arcade store."""
    
    def __init__(self, code: int, name: str, year_of_release: str, base_price: float, story_telling_creator: str, graphics_creator: str, category: str,difficulty:str,  number_of_players: int):
        super().__init__(code, name, year_of_release, base_price, story_telling_creator, graphics_creator, category, is_hd=False)
        self.difficulty = difficulty
        self.number_of_players = number_of_players

        def show_game_details(self):
            """
            Show the attributes of the Tetris Effect game, including the name, year of release, price,  difficulty, and number of players.
            """
            print(f"Game: {self.name}, Year of Release: {self.year_of_release}, Price: ${self.price}, Difficulty: {self.difficulty}, Number of Players: {self.number_of_players}")



class  FactoryGame:
    """
    This class represents a Factory of games from the Arcade store.
    """
    def __init__(self, game_name: str):

        def create_game(self, game_name):
            if game_name == "Dance Revolution":
                return DanceRevolutionGame()
            elif game_name == "Dancing Stage":
                return DancingStageGame()
            elif game_name == "Snake":
                return SnakeGame()
            elif game_name == "Tetris Effect":
                return TetrisEffectGame()
            elif game_name == "Need For Speed":
                return NeedForSpeedGame()
            elif game_name == "Ghost Squad":
                return GhostSquadGame()
            else:   
                return None
        
       