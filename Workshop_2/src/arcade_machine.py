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
    This class represents an arcade machine in the arcade store.

    Attributes:
        machine_code (int): A unique code to identify the machine.
        machine_name (str): The name of the arcade machine.
        machine_material (str): The material of the arcade machine.
        creation_year (str): The year the arcade machine was created.
        base_price (float): The base price of the arcade machine.
        color (str): The color of the arcade machine (set by the user).
        games (List): A list of games available on this arcade machine.
    """
    def __init__(self, machine_code:int, machine_name: str, machine_material: str, creation_year: str, base_price: float, color:str):
        self.machine_code = machine_code
        self.machine_name = machine_name
        self.machine_material = machine_material
        self.creation_year = creation_year
        self.base_price = base_price
        self.color = color
        self.dimensions = None
        self.weight = None
        self.power_consumption = None
        self.memory = None
        self.processor = None
        self.games = []

    def add_game(self, game:Game):
        """
        Adds a game to the arcade machine.

        Args:
            game (Game): The game to add to the arcade machine.
        """
        FactoryGame = FactoryGame()
        game = FactoryGame.create_game(game)
        self.games.append(game)
        self.base_price= self.base_price + game.base_price

    
    def remove_videogame(self, code: int, game:Game):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
        code (int): Code of the videogame to be removed.
        """
        index = -1 
        for i, vg in enumerate(self.games):
            if vg.get_code() == code:
                index = i
                break

        if index != -1: 
            self.games.pop(index)
            self.base_price= self.base_price - vg.base_price
        else:
            print(f"The videogame with the code {code} is not in the machine")

    def define_material(self, material: str):
        """
        Define the material of the arcade machine.

        Args:
            material (str): The material to assign to the arcade machine.
        """
        self.machine_material = material
    
    def change_price(self, material:str):
        if material == "wood":
            self.weight =self.weight+ self.weight* 0.10
            self.base_price= self.base_price-self.base_price*0.05
            self.power_consumption =self.power_consumption +self.power_consumption*0.15
        
        elif material == "aluminium":
            self.weight =self.weight-self.weight* 0.05
            self.base_price= self.base_price+self.base_price*0.10
        elif material == "carbon_fiber":
            self.weight =self.weight- self.weight* 0.15
            self.base_price= self.base_price+self.base_price*0.20
            self.power_consumption =self.power_consumption -self.power_consumption*0.10
        

    def select_color(self, color: str):
        """
        Select the color of the arcade machine.

        Args:
            color (str): The color to assign to the arcade machine.
        """
        self.color = color
    


    def change_name(self, name: str):
        """
        Change the name of the arcade machine.

        Args:
            name (str): The new name of the arcade machine.
        """
        self.machine_name = name

    def show_details(self):
        """


        Shows the details of the arcade machine, including its name, creation year, and price.
        """
        print(f"Arcade Machine: {self.machine_name}, Creation Year: {self.creation_year}, Price: ${self.base_price}, Color: {self.color}")


class DanceRevolutionMachine(ArcadeMachine):
    """
    This class represents a Dance Revolution arcade machine.

    Attributes:
        controls_price (float): The price of the machine's controls.
        difficulties (dict): Difficulty levels for the game.
        arrow_cardinalities (dict): Directions for the game arrows.
        dimensions (dict): The physical dimensions of the machine.
        weight (float): The weight of the machine.
        power_consumption (int): The power consumption of the machine.
        memory (int): The memory of the machine.
        processor (str): The processor of the machine.

    """
    def __init__(self, machine_code, machine_name , machine_material: str, base_price: float, controls_price: float, color: str, creation_year: str):
        super().__init__(machine_code, machine_name, machine_material, creation_year, base_price, color)
        self.machine_code = 1
        self.machine_name = "DanceRevolution"
        self.base_price = 5000000
        self.machine_material = machine_material
        self.controls_price = 200000
        self.difficulties = {1: "Easy", 2: "Normal", 3: "Hard", 4: "Extreme"}
        self.arrow_cardinalities = {1: "Up", 2: "Left", 3: "Right", 4: "Down"}
        self.dimensions = {"width": 80, "length": 100, "height": 180}
        self.weight = 60  # kg
        self.power_consumption = 200  # watts
        self.memory = 8  # GB
        self.processor = "Quad-Core 2.5 GHz"
        self.color = color
        self.creation_year = 2001


class ClassicalMachine(ArcadeMachine):
    """
    This class represents a classical arcade machine.

    Attributes:
        dimensions (dict): The physical dimensions of the machine.
        weight (float): The weight of the machine.
        power_consumption (int): The power consumption of the machine.
        memory (int): The memory of the machine.
        processor (str): The processor of the machine.

    """
    def __init__(self, machine_code: int, machine_name: str, machine_material: str, creation_year: str, base_price: float, color: str):
        super().__init__(machine_code, machine_name, machine_material, creation_year, base_price, color)
        self.machine_code = 2
        self.machine_name = "ClassicalMachine"
        self.base_price = 3000000
        self.machine_material = machine_material
        self.creation_year = 1980
        self.color = color
        self.dimensions = {"width": 60, "length": 80, "height": 160}
        self.weight = 70.0  # kg
        self.power_consumption = 300  # watts
        self.memory = 4  # GB
        self.processor = "Dual-Core 1.8 GHz"

    def make_vibration(self):
        """
        Simulates a vibration  for the machine.
        """
        return True

    def sound_record_alert(self):
        """
        Triggers a sound recording alert  for the machine.
        """
        return "Recording activated"


class VirtualRealityMachine(ArcadeMachine):
    """
    This class represents a virtual reality arcade machine.

    Attributes:
        glasses_type (str): The type of VR glasses.
        glasses_resolution (str): The resolution of the VR glasses.
        glasses_price (float): The price of the VR glasses.
        dimensions (dict): The physical dimensions of the machine.
        weight (float): The weight of the machine.
        power_consumption (int): The power consumption of the machine.
        memory (int): The memory of the machine.
        processor (str): The processor of the machine.

    """
    def __init__(self, machine_code: int, machine_name: str, machine_material: str, base_price: float, creation_year: str, glasses_type: str, glasses_resolution: str, glasses_price: float, color: str):
        super().__init__(machine_code, machine_name, machine_material, creation_year, base_price, color)
        self.machine_code = 3
        self.machine_name = "VirtualRealityMachine"
        self.base_price = 7000000
        self.creation_year = 2016
        self.color = color
        self.glasses_type = "Vision 2"
        self.glasses_resolution = "4K"
        self.glasses_price = 300000
        self.dimensions = {"width": 100, "length": 100, "height": 200}
        self.weight = 7.0  # kg
        self.power_consumption = 200  # watts
        self.memory = 16  # GB
        self.processor = "Octa-Core 3.2 GHz"


class ShootingMachine(ArcadeMachine):
    """
    This class represents a shooting arcade machine.

    Attributes:
        toy_gun_price (float): The price of the toy gun for the shooting machine.
    """
    def __init__(self, machine_code: int, machine_name: str, machine_material: str, base_price: float, creation_year: str, toy_gun_price: float, color: str):
        super().__init__(machine_code, machine_name, machine_material, creation_year, base_price, color)
        
        self.machine_code = 4
        self.machine_name = "ShootingMachine"
        self.base_price = 4000000
        self.creation_year = 1990
        self.color = color
        self.machine_material = machine_material
    
        self.toy_gun_price = 200000
        self.dimensions = {"width": 70, "length": 120, "height": 180}
        self.weight = 60  # kg
        self.power_consumption = 200  # watts
        self.memory = 6  # GB
        self.processor = "Quad-Core 2.8 GHz"


class RacingMachine(ArcadeMachine):
    """
    This class represents a racing arcade machine.

    Attributes:
        toy_steering_wheel_price (float): The price of the toy steering wheel.
    """
    def __init__(self, machine_code: int, machine_name: str, machine_material: str, base_price: float, creation_year: str, toy_steering_wheel_price: float, color: str):
        super().__init__(machine_code, machine_name, machine_material, creation_year, base_price, color)
        
        
        self.machine_code = 5
        self.machine_name = "RacingMachine"
        self.machine_material = machine_material
        self.color = color
        self.base_price = 6000000
        self.creation_year = 1995
        self.toy_steering_wheel_price = 200000
        self.dimensions = {"width": 120, "length": 150, "height": 160}
        self.weight = 60  # kg
        self.power_consumption = 200  # watts
        self.memory = 12  # GB
        self.processor = "Quad-Core 3.0 GHz"

class FactoryArcadeMachine:

    """
    This class represents a factory of arcade machines.
    Attributes:
        machine_name (str): The name of the arcade machine.
    """
    def __init__(self, machine_name: str):
        def create_machine(self, machine_name: str):
            if machine_name == "DanceRevolution":
                return DanceRevolutionMachine()
            elif machine_name == "Classical":
                return ClassicalMachine()
            elif machine_name == "VirtualReality":
                return VirtualRealityMachine()
            elif machine_name == "Shooting":
                return ShootingMachine()
            elif machine_name == "Racing":
                return RacingMachine()
            else:
                return None    
        

