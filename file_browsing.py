import os
import csv
from typing import List, Tuple

import csv_creator

def create_files(triples: List[Tuple[str, str, str]]) -> List[str]:
    """
    Creates directories and CSV files based on the provided triples.

    For each triple (month, day, time) in the input, this function:
    1. Creates a directory structure based on the month and day if it doesn't already exist.
    2. Creates an empty CSV file named after the time inside the created directory.
    3. If the file already exists, it prints a message indicating that the file will be overwritten.
    4. Returns a list of paths to the created files.

    Args:
        triples (List[Tuple[str, str, str]]): A list of tuples, where each tuple contains three strings (month, day, time).

    Returns:
        List[str]: A list of paths to the created files.
    """
    file_paths = []  # List to store paths of created files

    for month, day, time in triples:
        # Create directory if doesn't exist
        dir_path = os.path.join(month, day, time)
        os.makedirs(dir_path, exist_ok=True)

        # Create the path and add to return list
        file_path = os.path.join(dir_path, f"Dane.csv")
        file_paths.append(file_path)

        # If file present print info, otherwise create it
        if not os.path.exists(file_path):
            csv_creator.write_random_csv(file_path)
        else:
            print(
                f"file {file_path} already found, it's contents will be overwritten")
            csv_creator.write_random_csv(file_path)

    return file_paths


def check_and_sum(triples: List[Tuple[str, str, str]], verbose: bool = True) -> int:
    """
    Checks for the existence of CSV files based on the provided triples and sums the "Czas" values where "Model" is "A".

    For each triple (month, day, time) in the input, this function:
    1. Constructs the file path based on the month, day, and time.
    2. Checks if the file exists:
       - If the file does not exist prints a message indicating the missing file.
       - If the file exists, reads the file and sums the "Czas" values where "Model" is "A".
    3. Returns the total sum of "Czas" values where "Model" is "A".
    4. If verbose is True (i.e. by default) also prints the result

    Args:
        triples (List[Tuple[str, str, str]]): A list of tuples, where each tuple contains three strings (month, day, time).
        verbose (bool): If True, prints the computed result

    Returns:
        int: The total sum of "Czas" values where "Model" is "A".
    """
    total_time = 0

    for month, day, time in triples:
        file_path = os.path.join(month, day, time, f"Dane.csv")

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
        else:
            # If the file exists, read it and sum "Czas" where "Model" is "A"
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    if row["Model"] == "A":
                        czas_value = row["Czas"].replace(
                            's', '')  # remove the 's' suffix
                        total_time += int(czas_value)  # sum the values

    if verbose:
        print(f"Total Czas for 'A' models: {total_time}s")
    return total_time
