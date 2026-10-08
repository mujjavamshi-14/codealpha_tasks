# Stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

# Get stock name from user
stock_name = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()

# Get quantity
quantity = int(input("Enter quantity: "))

# Check if stock exists
if stock_name in stocks:

    # Calculate total investment
    total = stocks[stock_name] * quantity

    print("Stock Price:", stocks[stock_name])
    print("Quantity:", quantity)
    print("Total Investment:", total)

else:
    print("Stock not found!")
