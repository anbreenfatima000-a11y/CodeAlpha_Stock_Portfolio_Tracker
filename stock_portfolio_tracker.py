stock_prices = {
    "AAPL": 180,
    "GOOGL": 250,
    "MSFT": 300
}

total_investment = 0
portfolio = []

while True:

    input_stock = input(
        "Enter the stock symbol (AAPL, GOOGL, MSFT): "
    ).upper()

    if not input_stock.isalpha():
        print("Please enter a valid stock symbol.")
        continue

    if input_stock not in stock_prices:
        print("Invalid stock symbol. Please enter a valid stock symbol.")
        continue

    while True:
        try:
            input_quantity = int(
                input("Enter the quantity of shares: ")
            )
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if input_quantity <= 0:
            print("Please enter a quantity greater than 0.")
            continue

        break

    portfolio.append((input_stock, input_quantity))

    total_investment += stock_prices[input_stock] * input_quantity

    print(
        f"{input_quantity} shares of {input_stock} "
        f"= ${stock_prices[input_stock] * input_quantity}"
    )

    while True:
        user_answer = input(
            "Add another stock? (yes/no): "
        ).lower()

        if user_answer not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
            continue

        break

    if user_answer == "no":
        print(f"\nThe total investment is: ${total_investment}")
        break


with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio:
        investment = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares = ${investment}\n"
        )

    file.write(
        f"\nTotal Investment: ${total_investment}\n"
    )

print("Portfolio saved to portfolio.txt")