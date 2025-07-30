"""
Stock Portfolio Tracker
Author: Kousika Sabarisha
Description:
    A Python script to calculate and summarize the user's total stock investment.
    It uses hardcoded stock prices and allows users to input their holdings.
    Results can be saved to both text and CSV files.
"""

import csv

# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 310
}

def collect_portfolio():
    """Prompts user to enter their stock holdings."""
    print("📈 Stock Portfolio Tracker")
    print("Available Stocks:", ', '.join(STOCK_PRICES.keys()))
    print("Enter your stock holdings. Type 'done' to finish.\n")

    portfolio = {}

    while True:
        stock = input("Enter Stock Symbol: ").strip().upper()
        if stock == 'DONE':
            break
        if stock not in STOCK_PRICES:
            print("❌ Invalid stock. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("⚠️ Please enter a valid number.")

    return portfolio

def display_summary(portfolio):
    """Calculates and displays portfolio summary."""
    total_investment = 0
    summary_lines = []

    print("\n📊 Portfolio Summary:")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * qty
        total_investment += investment
        line = f"{stock}: {qty} x ${price} = ${investment}"
        summary_lines.append(line)
        print(line)

    print(f"\n💰 Total Investment: ${total_investment}")
    return summary_lines, total_investment

def save_to_files(summary, total, txt_filename="portfolio.txt", csv_filename="portfolio.csv"):
    """Saves portfolio to text and CSV files."""
    # Save to text
    with open(txt_filename, "w") as f:
        f.write("Stock Portfolio Summary\n------------------------\n")
        for line in summary:
            f.write(line + "\n")
        f.write(f"\nTotal Investment: ${total}")

    # Save to CSV
    with open(csv_filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])
        for line in summary:
            parts = line.split()
            writer.writerow([parts[0][:-1], parts[1], parts[3].strip('$'), parts[-1].strip('$')])
        writer.writerow([])
        writer.writerow(["Total", "", "", total])

    print(f"\n✅ Portfolio saved as '{txt_filename}' and '{csv_filename}'")

def main():
    portfolio = collect_portfolio()
    if not portfolio:
        print("No data entered. Exiting.")
        return

    summary, total = display_summary(portfolio)
    save = input("\nDo you want to save the report? (yes/no): ").strip().lower()
    if save == 'yes':
        save_to_files(summary, total)

if __name__ == "__main__":
    main()
