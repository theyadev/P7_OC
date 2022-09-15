from typings import Shares


def get_shares_cost(shares: Shares):
    prices = []
    for share in shares:
        prices.append(share[1])

    return sum(prices)
