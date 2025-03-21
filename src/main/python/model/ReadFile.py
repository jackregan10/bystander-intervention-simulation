from pathlib import Path
import re

class ReadFile:
    """
    This class reads the input file and extracts the single values from it.
    
    Author: Jack Regan
    """
    def __init__ (self, file_path):
        self.single_values = {}
        try:
            self.file_path = Path(file_path)
        except FileNotFoundError as e:
            print(f"File reading error: {e}")
    def read_file (self):
        """
        Reads csv file into a pandas data frame called input_data
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                numbers = [float(n) if '.' in n else int(n) for n in numbers]
                comment_match = re.search(r"/\*\s*(.*?)\s*\*/", line)
                param_name = comment_match.group(1) if comment_match else f"param_{len(self.single_values) + 1}"
                if len(numbers) == 1:
                    self.single_values[param_name] = numbers[0]
                else:
                    print(f"Warning: Unexpected format in line -> {line.strip()}")
    def get_single_values(self):
        """
        Retrieve the single values from the file.

        Returns:
            list: A list containing the single values.
        """
        return self.single_values
