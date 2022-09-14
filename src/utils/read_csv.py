from csv import reader

def isfloat(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False

def read_csv(filename: str):
    try:
        with open(filename) as file:
            csv_reader = reader(file)
            
            data = []

            for row in csv_reader:
                (name, price, profit) = row

                if not isfloat(price) or not isfloat(profit):
                    continue

                price, profit = float(price), float(profit)

                if price <= 0 or profit <= 0:
                    continue

                data.append((name, price, profit))

            return data
    except FileNotFoundError:
        print(f"{filename} not found.")
        exit(1)
