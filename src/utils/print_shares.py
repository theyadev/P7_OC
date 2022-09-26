from time import time

from typings import Shares

from utils.get_shares_cost import get_shares_cost
from utils.get_shares_profit import get_shares_profit


def print_shares(shares: Shares,
                 start_time: float,
                 price: float = None,
                 profit: float = None):
    print(f"\nVoici dans quels actions il faut investir ({len(shares)} actions) :\n")

    for share in shares:
        print(f"{share[0]} | {share[1]} € | + {share[2]} %")

    if not price:
        price = get_shares_cost(shares)

    if not profit:
        profit = get_shares_profit(shares)

    print("\nCout total : ", round(price, 2), "€")
    print("Profit : +", round(profit, 2), "€")
    print("\nTemps d'execution : ", round(time() - start_time, 4), "seconds")
