"""
Problem:
U want to perform various calculations (e.g., min, max, etc.) on a dictionary of data.
"""
prices = {
    'ACME': 45.21,
    'AAPL': 612.87,
    'IBM"': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))