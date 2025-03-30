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
        parameters = file_reader.get_single_values()
        model = Model(parameters)
        output_data = model.run_routine()
        output_parameters = pd.DataFrame(
            {
                "Agents": [parameters["Agents"]],
                "Simulations": [parameters["Simulations"]],
                "Maximum Loop Iterations": [parameters["Maximum Loop Iterations"]],
                "Intoxication Level Increment": [parameters["Intoxication Level Increment"]]
            }
        )
        file_writer = WriteFile()
        file_writer.write_file(output_parameters, output_data)

if __name__ == "__main__":
    simulation = Driver()
    simulation.run_model()
