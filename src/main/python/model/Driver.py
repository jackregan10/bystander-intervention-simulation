from ReadFile import ReadFile
from WriteFile import WriteFile
from Model import Model

import pandas as pd

class Driver:
    """
    This class serves as the driver for the model. It reads in the 
    parameters from the input file, calls the routine, and writes the 
    output data to the output file.
    
    Author: Jack Regan
    """
    def run_model(self):
        """
        This method reads in the parameters from the input file, calls the
        routine, and writes the output data to the output file.
        """
        file_reader = ReadFile("src/main/resources/simulation_input.txt")
        file_reader.read_file()
        
        file_writer = WriteFile()
        file_writer.write_file()
if __name__ == "__main__":
    simulation = Driver()
    simulation.run_model()
