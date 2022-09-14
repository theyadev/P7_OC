from utils.get_shares_cost import get_shares_cost
from utils.get_shares_profit import get_shares_profit

from time import time

def print_shares(shares: list[str, float, float], start_time: float, price: int = None, profit: int = None):
    print(f"\nMost profitable investment ({len(shares)} shares) :\n")

    for share in shares:
        print(f"{share[0]} | {share[1]} € | +{share[2]} %")

    if not price:
        price = get_shares_cost(shares)

    if not profit:
        profit = get_shares_profit(shares)

    print("\nTotal cost : ", price, "€")
    print("Profit after 2 years : +", round(profit, 2), "€")
    print("\nTime elapsed : ", round(time() - start_time, 4), "seconds")
