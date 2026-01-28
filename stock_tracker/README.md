📊 Stock Portfolio Tracker Using Python
📌 Project Overview

This project calculates the total investment value of a user’s stock portfolio using Python. Users input stock symbols and quantities, and the program computes the investment based on hardcoded stock prices. Optionally, the results can be saved to a file.

🎯 Goal

Automate stock investment calculations and provide a simple, beginner-friendly Python program.

🛠️ Key Concepts Used

Dictionary → stores stock prices

Input/Output → user interaction

Arithmetic operations → calculate total investment

File handling (optional) → save results

Loops & Conditionals → validate input and process multiple stocks

💻 Python Code (Short Version)
stock_prices = {"AAPL":180, "TSLA":250, "GOOGL":100, "MSFT":150}
total_investment = 0
portfolio = {}

n = int(input("Enter number of stocks: "))
for i in range(n):
    stock = input(f"Stock #{i+1}: ").upper()
    qty = int(input(f"Quantity of {stock}: "))
    if stock in stock_prices:
        inv = stock_prices[stock]*qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${inv}")
        total_investment += inv
        portfolio[stock] = qty
    else:
        print(f"{stock} price not found, skipping.")

print(f"\nTotal investment: ${total_investment}")

if input("Save to file? (yes/no): ").lower() == "yes":
    with open("portfolio.txt","w") as f:
        f.write("Stock Portfolio Summary\n------------------------\n")
        for s,q in portfolio.items():
            f.write(f"{s}: {q} shares x ${stock_prices[s]} = ${stock_prices[s]*q}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")

📊 Sample Output
Stock #1: AAPL
Quantity of AAPL: 5
AAPL: 5 shares x $180 = $900
Stock #2: TSLA
Quantity of TSLA: 2
TSLA: 2 shares x $250 = $500
Total investment: $1400
Portfolio saved to portfolio.txt

✅ Advantages

Quickly calculates stock investments

Easy to use and beginner-friendly

Optionally saves portfolio for future reference

❌ Limitations

Hardcoded stock prices (not real-time)

Cannot handle invalid quantity input automatically

🚀 Future Enhancements

Fetch real-time stock prices via API

Add GUI for better user experience

Save in CSV format for Excel analysis

👩‍💻 Author

Kokila