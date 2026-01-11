# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300
}

# Function to get user input for stocks
def get_portfolio():
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not available. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Invalid quantity. Try again.")
    return portfolio

# Function to calculate total investment
def calculate_total(portfolio):
    total = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        stock_value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_value}")
        total += stock_value
    print(f"\nTotal Investment: ${total}")
    return total

# Optionally save to a file
def save_to_file(portfolio, total):
    choice = input("Do you want to save this portfolio to a file? (yes/no): ").lower()
    if choice == "yes":
        filename = input("Enter filename (with .txt or .csv): ")
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            f.write(f"\nTotal Investment,,,{total}\n")
        print(f"Portfolio saved to {filename}")

# Main program
portfolio = get_portfolio()
if portfolio:
    total = calculate_total(portfolio)
    save_to_file(portfolio, total)
else:
    print("No stocks entered.")
