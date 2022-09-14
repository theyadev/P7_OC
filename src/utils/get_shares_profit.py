def get_shares_profit(shares: list[str, float, float]):
    profits = []
    for share in shares:
        profits.append(share[1] * share[2] / 100)

    return sum(profits)
