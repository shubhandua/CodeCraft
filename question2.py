def max_profit(prices):
    if not prices:
        return 0  # No prices available

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)  # Track the lowest price so far
        max_profit = max(max_profit, price - min_price)  # Max profit if sold today

    return max_profit

# Example Usage
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output: 5 (Buy at 1, Sell at 6)
