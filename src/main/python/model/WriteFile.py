from genericpath import exists
import pandas as pd


class WriteFile:
    """
    Saves output data frame as a csv called "Defection-Simulation-Output.csv"
    The file is saved to the output folder.
        
    Author: Jack Regan
    """
    def write_file (self, output_parameters, output_data):
        """
        Writes the output data to a csv file called "Defection-Simulation-Output.csv"
        The file is saved to the output folder.

        Args:
            output_parameters (DataFrame): Holds parameters and headers.
            output_data (DataFrame): Holds output data and headers.

        Raises:
            ValueError: throws an error if the output data is not a Pandas DataFrame.
        """
        try:
           if not  isinstance(output_data, pd.DataFrame) and isinstance(output_parameters, pd.DataFrame):
                raise ValueError("Output data must be a Pandas DataFrame.")
        except TypeError:
            print("Output data reading error")
            return
        try:
            out_file = "src/main/output/Defection-Simulation-Output.xlsx"
            if exists(out_file):
                i = 1
                out_file = "src/main/output/Defection-Simulation-Output-" + str(i) + ".xlsx"
                while exists(out_file):
                    i += 1
                    out_file = "src/main/output/Defection-Simulation-Output-" + str(i) + ".xlsx"
            with pd.ExcelWriter(out_file, engine = "openpyxl") as writer:       
                output_parameters.to_excel(writer, sheet_name = "Parameter Data", index = False)
                output_data.to_excel(writer, sheet_name = "Output Data", index=False)
        
        except ValueError as e:
            print(f"ValueError: {str(e)}")
        except IOError as e:
            print(f"IOError: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
