def wall_street_naive(prices):
    """returns the maximum amount of profit possible"""
    # will hold all potential profits
    potential_profits = []
    # O(n) loop
    for i in range(len(prices)):
        buy = prices[i]
        # O(n - i) loop inside O(n) loop -- O(n^2)
        for j in range(i, len(prices)):
            sell = prices[j]
            profit = sell - buy
            if profit > 0:
                # O(n) worst-case operation in O(n^2) loop...
                # that's O(n^3) worst-case...
                # super discrete problem here, easy to overlook
                potential_profits.append(profit)
    # O(n) operation, but not nested so this call to __max__ is fine
    return max(potential_profits)


def wall_street_better(prices):
    length = len(prices)

    # check if we have less than two days of records
    if length < 2:
        # cannot buy on same day, no profits
        return

    max_cost = 0
    min_price = prices[0]
    # O(n)
    for i in range(length):
        # O(2) -- only picking smallest of 2 elements
        min_price = min(min_price, prices[i])

        # O(2) -- only picking largest of 2 elements
        max_cost = max(max_cost, prices[i] - min_price)

    return max_cost


def buy_and_sell_recurse(prices_lst, profits=None):
    if not profits:
        profits = []

    buy = prices_lst[0]

    for i in range(1, len(prices_lst)):
        sell = prices_lst[i]
        new_profit = sell - buy
        profits.append(new_profit)

    prices_lst = prices_lst[1:]

    if len(prices_lst) == 1:
        return max(profits)

    return buy_and_sell_recurse(prices_lst, profits)


if __name__ == '__main__':
    import timeit

    t1_prices = [7, 1, 5, 3, 6, 4]
    print(timeit.timeit("wall_street_naive(t1_prices)", globals=globals()))
    print(timeit.timeit("wall_street_better(t1_prices)", globals=globals()))
    print(timeit.timeit("buy_and_sell_recurse(t1_prices)", globals=globals()))
