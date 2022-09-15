from time import time

from typings import Shares

from utils.read_csv import read_csv
from utils.print_shares import print_shares

def main():
    MONEY = 500

    shares = read_csv("./data/dataset2.csv")

    start_time = time()

    lowest_price = min(shares, key=lambda x: x[1])[1]

    sorted_shares = sorted(shares, key=lambda x: x[2], reverse=True)

    buyed_shares: Shares = []

    for share in sorted_shares:
        if share[1] <= MONEY:
            buyed_shares.append(share)
            MONEY -= share[1]

        if MONEY < lowest_price:
            break

    print_shares(buyed_shares, start_time)


if __name__ == '__main__':
    main()
