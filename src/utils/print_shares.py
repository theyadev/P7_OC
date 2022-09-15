from time import time

from typings import Shares

from utils.get_shares_cost import get_shares_cost
from utils.get_shares_profit import get_shares_profit


def print_shares(shares: Shares,
                 start_time: float,
                 price: float = None,
                 profit: float = None):
    print(f"\nMost profitable investment ({len(shares)} shares) :\n")

    for share in shares:
        print(f"{share[0]} | {share[1]} € | +{share[2]} %")

    if not price:
        price = get_shares_cost(shares)

    if not profit:
        profit = get_shares_profit(shares)

    print("\nTotal cost : ", round(price, 2), "€")
    print("Profit after 2 years : +", round(profit, 2), "€")
    print("\nTime elapsed : ", round(time() - start_time, 4), "seconds")
