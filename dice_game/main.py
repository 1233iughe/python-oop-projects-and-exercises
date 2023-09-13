import random

class Dice:
    """
    Class representing the dice in the game.
    """

    def __init__(self) -> None:
        """
        Creates Dice instance with default value.
        """
        
        self._value = None
    
    @property
    def value(self):
        """
        Sets a getter for the protected attribute _value.
        Getter is not defined as is not intended to be modified outside the class.
        """
        return self._value
    
    def roll(self):
        """
        Rolls the dice and sets _value attribute to a random number between 1 and 6 
        """
        new_value = random.randint(1, 6)
        self._value = new_value
        return self


testDice = Dice()

print([testDice.roll().value for i in range(10)])