
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320,
    "AMZN": 3500
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!\n")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you're finished entering stocks.\n")


while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not recognized. Please try again.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity must be non-negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")


print("\nYour Portfolio Summary:")
print("------------------------")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print("------------------------")
print(f"Total Investment Value: ${total_value}")


save = input("\nWould you like to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"Total,,,{total_value}\n")
    print(f"Portfolio saved to {filename}")