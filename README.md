# 💰 Smart Expense Tracker

A simple and user-friendly **Python-based Expense Tracker** that helps users record their income and expenses, analyze spending habits, and understand their financial balance.

This project demonstrates practical applications of **Python, Pandas, CSV file handling, data analysis, and data visualization**.

---

## 📌 Project Overview

Managing daily expenses manually can make it difficult to understand where money is being spent.

The **Smart Expense Tracker** provides a simple command-line solution where users can:

* Add income and expenses
* View all transactions
* Calculate total income
* Calculate total expenses
* Calculate remaining balance
* Analyze expenses by category
* Search transactions
* Generate an expense visualization

All transaction data is stored locally in a CSV file.

---

## ✨ Features

### 1. Add Transaction

Users can add:

* Income
* Expense
* Category
* Amount
* Description

The transaction is automatically saved with the current date.

### 2. View Transactions

Displays all recorded transactions in a structured table.

### 3. Financial Summary

The application calculates:

```text
Total Income
Total Expenses
Remaining Balance
```

The balance is calculated using:

```text
Balance = Total Income - Total Expenses
```

### 4. Category Analysis

Expenses are grouped by category to identify spending patterns.

For example:

```text
Food          ₹750
Transport     ₹350
Education     ₹1200
Shopping      ₹850
```

The application also identifies the highest spending category.

### 5. Expense Visualization

The project generates a bar chart showing the amount spent in each category.

The chart is saved as:

```text
expense_chart.png
```

### 6. Search Transactions

Users can search transactions using:

* Category
* Description

---

## 🛠️ Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Core programming language           |
| Pandas     | Data processing and analysis        |
| Matplotlib | Data visualization                  |
| CSV        | Local data storage                  |
| Git/GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
Smart-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── requirements.txt
├── README.md
└── expense_chart.png
```

---

## ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Expense-Tracker.git
```

### Step 2: Open the project folder

```bash
cd Smart-Expense-Tracker
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the program

```bash
python expense_tracker.py
```

---

## 🖥️ How to Use

After running the program, the following menu appears:

```text
==========================================
       SMART EXPENSE TRACKER
==========================================
1. Add Transaction
2. View Transactions
3. Financial Summary
4. Category Analysis
5. Generate Expense Chart
6. Search Transactions
7. Exit
==========================================
```

Enter the number corresponding to the required operation.

---

## 📊 Example

Suppose the user has:

```text
Income = ₹25,000
Expenses = ₹3,650
```

The application calculates:

```text
Balance = ₹25,000 - ₹3,650
        = ₹21,350
```

The application can also determine which category has the highest spending.

---

## 🧠 Concepts Demonstrated

This project demonstrates several important Python concepts:

* Variables
* Functions
* Conditional statements
* Loops
* Exception handling
* File handling
* CSV data processing
* Pandas DataFrames
* Data filtering
* Data grouping
* Data aggregation
* Data visualization
* User input validation
* Modular programming

---

## 🔮 Future Improvements

The project can be extended with:

* Monthly expense reports
* Budget limits
* Login system
* SQLite database
* Graphical User Interface using Tkinter
* Web application using Flask
* Machine Learning based expense prediction
* Automatic spending recommendations
* PDF financial reports

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

1. Build a complete Python application.
2. Store and retrieve structured data.
3. Analyze data using Pandas.
4. Create visualizations using Matplotlib.
5. Handle invalid user input.
6. Organize Python code using functions.
7. Manage a project using Git and GitHub.

---

## 👩‍💻 Author

**Rachana Y**

B.Tech – Computer Science and Engineering
Specialization: Artificial Intelligence & Machine Learning

---

## 📜 License

This project is created for educational and portfolio purposes.
