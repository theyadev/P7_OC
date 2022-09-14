def get_shares_cost(shares: list[str, float, float]):
    prices = []
    for share in shares:
        prices.append(share[1])

    return sum(prices)
