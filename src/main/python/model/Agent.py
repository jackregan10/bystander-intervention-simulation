import numpy as np


class Agent:
    """
    A class to represent an agent in the model.

    Attributes
    ----------
    internal_pressure : float
        the internal pressure of the agent to intervene in a crisis

    Author: Jack Regan
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the agent object.
        """
        self.internal_pressure = np.random.uniform(0.2, 0.5)

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
