# CodeAlpha Stock Portfolio Tracker

A simple **Python-based Stock Portfolio Tracker** developed as part of my **CodeAlpha Internship**.

This project allows users to enter stock symbols and the number of shares they own. It calculates the investment for each stock, keeps track of the total investment, and saves the final portfolio summary in a text file.

## Features

* Supports predefined stock symbols: **AAPL, GOOGL, and MSFT**.
* Allows users to enter the number of shares.
* Validates stock symbols and user input.
* Prevents invalid or non-positive share quantities.
* Calculates the investment value for each stock.
* Allows multiple stocks to be added to the portfolio.
* Calculates the total investment.
* Saves the portfolio details to `portfolio.txt`.

## Technologies Used

* **Python 3**
* File Handling
* Dictionaries
* Lists
* Loops
* Input Validation

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:

```bash
git clone https://github.com/your-username/CodeAlpha_StockPortfolioTracker.git
```

3. Open the project folder:

```bash
cd CodeAlpha_StockPortfolioTracker
```

4. Run the program:

```bash
python stock_portfolio_tracker.py
```

## How It Works

The program starts with a predefined list of stock prices:

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| GOOGL |  $250 |
| MSFT  |  $300 |

The user enters a stock symbol and the number of shares. The program then calculates the investment value using:

```text
Investment = Stock Price × Number of Shares
```

Users can continue adding stocks until they choose **no**.

At the end, the program displays the total investment and creates a `portfolio.txt` file containing the portfolio summary.

## Output File

The program automatically creates:

```text
portfolio.txt
```

The file contains the selected stocks, number of shares, individual investment values, and the total investment.

## Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```

> `portfolio.txt` is generated automatically after running the program.

## Internship Task

This project was completed as part of the **CodeAlpha Python Programming Internship**.

The project helped me practice:

* Python dictionaries
* Lists and tuples
* `while` loops
* Conditional statements
* User input and validation
* Exception handling
* Basic calculations
* File handling in Python

## Author

**Anbreen Fatima**

BS Information Technology Student
Python Programming Intern — CodeAlpha

