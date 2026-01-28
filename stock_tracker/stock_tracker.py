# Stock Portfolio Tracker
# Author: Kokila
# Goal: Calculate total investment based on manually defined stock prices

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 100,
    "MSFT": 150
}

# Step 2: Initialize total investment and user portfolio
total_investment = 0
portfolio = {}

# Step 3: Ask user for number of stocks
try:
    n = int(input("Enter number of stocks you want to input: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Step 4: Loop to get stock symbol and quantity
for i in range(n):
    stock = input(f"Stock #{i+1} symbol: ").upper()
    
    try:
        quantity = int(input(f"Quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity! Please enter a number. Skipping this stock.")
        continue

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}")
        total_investment += investment
        portfolio[stock] = quantity
    else:
        print(f"{stock} price not found in our system. Skipping this stock.")

# Step 5: Display total investment
print(f"\nTotal investment value: ${total_investment}")

# Step 6: Optional - Save portfolio to a file
save_file = input("Do you want to save the portfolio to a file? (yes/no): ").lower()

if save_file == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            investment = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")

print("\nThank you for using the Stock Portfolio Tracker!")
