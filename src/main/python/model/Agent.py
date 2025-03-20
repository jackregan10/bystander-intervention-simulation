import random

class Agent:
    """
    A class to represent an agent in the model.
    
    Author: Jack Regan
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the agent object.

        Args:
            internal_pressure (_float_): the internal pressure of the agent to intervene in a crisis
        """
        self.internal_pressure = random.randint(0, 100)
    def get_internal_pressure(self):
        """
        Get the internal pressure of the agent to intervene in a crisis.

        Returns:
            _float_: the internal pressure of the agent to intervene in a crisis
        """
        return self.internal_pressure
    def set_internal_pressure(self, internal_pressure):
        """
        Set the internal pressure of the agent to intervene in a crisis.

        Args:
            internal_pressure (_float_): the internal pressure of the agent to intervene in a crisis
        """
        self.internal_pressure = internal_pressure
