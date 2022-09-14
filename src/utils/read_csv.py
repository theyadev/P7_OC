from csv import reader

def read_csv(filename: str):
    try:
        with open(filename) as file:
            csv_reader = reader(file)

            # Skip first row
            next(file)

            data = list(
                map(lambda row: (row[0], float(row[1]), float(row[2])), csv_reader))

            return data
    except FileNotFoundError:
        print(f"{filename} not found.")
        exit(1)
