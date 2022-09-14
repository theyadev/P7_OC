
from itertools import combinations
from progress.bar import Bar
from time import time

from utils.get_shares_cost import get_shares_cost
from utils.get_shares_profit import get_shares_profit
from utils.print_shares import print_shares
from utils.read_csv import read_csv

MONEY = 500

def find_best_shares(shares: list[str, float, float]):
    profit = 0
    price = 0
    best_shares = []

    bar = Bar("Bruteforcing", max=len(shares))

    for i in range(len(shares)):
        share_combinations = combinations(shares, i + 1)

        for combination in share_combinations:
            shares_price = get_shares_cost(combination)
            
            if shares_price > MONEY:
                continue

            shares_profit = get_shares_profit(combination)

            if profit > shares_profit:
                continue

            profit = shares_profit
            best_shares = combination
            price = shares_price
        
        bar.next()
    
    return (best_shares, price, profit)

def main():
    shares = read_csv("./data/shares_1.csv")

    start_time = time()

    (best_shares, price, profit) = find_best_shares(shares)

    print_shares(best_shares, start_time, price, profit)



        

if __name__ == '__main__':
    main()