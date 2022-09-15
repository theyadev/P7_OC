from typings import Shares


def get_shares_profit(shares: Shares):
    profits = []
    for share in shares:
        profits.append(share[1] * share[2] / 100)

    return sum(profits)
