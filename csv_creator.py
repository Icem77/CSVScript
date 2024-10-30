import csv
import random
from typing import List, Tuple

def write_random_csv(file_path: str):
    """Writes a CSV file with a header and one row of random data."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow(["Model", "Wynik", "Czas"])
        # Write random data
        model = random.choice(["A", "B", "C"])
        wynik = random.randint(0, 1000)
        czas = f"{random.randint(0, 1000)}s"
        writer.writerow([model, wynik, czas])
