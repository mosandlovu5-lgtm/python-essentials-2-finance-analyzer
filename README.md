# Personal Finance Transaction Analyzer

## Overview
The Personal Finance Transaction Analyzer is a Python application that reads and analyzes bank transaction data. The program is designed to handle messy real-world financial records by validating data, detecting errors, tracking balances, identifying duplicates, and generating summary reports.

This project was developed as part of the Melsoft Academy Python Essentials 2 Advanced Challenge.

---

## Features

### Transaction Management
- Load and validate transaction records
- Normalize incorrect date formats
- Reject invalid or incomplete records
- Handle missing files safely

### Financial Analysis
- Running balance ledger using generators
- Category-based spending and income totals
- Duplicate transaction detection
- Statistical outlier detection

### Reporting
- Monthly summary reports
- Environment and date stamps
- Analyzer run logs

### Testing
- Assertion-based test suite
- Validation of edge cases
- Automated pass/fail reporting

---

## Project Structure

```text
python-essentials-2-finance-analyzer/
│
├── main.py
├── models.py
├── parser.py
├── analytics.py
├── reporting.py
├── tests.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Generators
- Closures
- File Handling
- Statistics Module
- Git & GitHub

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mosandlovu5-lgtm/python-essentials-2-finance-analyzer.git
```

2. Navigate into the project:

```bash
cd python-essentials-2-finance-analyzer
```

3. Run the application:

```bash
python main.py
```

4. Run the test suite:

```bash
python tests.py
```

---

## Menu Options

1. Generate a messy sample statement file
2. Load and validate transactions
3. Show running balance ledger
4. Display category breakdown
5. Detect duplicate transactions
6. Flag unusual transactions
7. Generate monthly summary report
8. Run self-tests
9. Exit

---

## Example Transaction

```text
2026-08-01 Salary 15000.00 INCOME
```

---

## Learning Outcomes

This project demonstrates:

- Defensive programming
- Data validation
- Error handling
- Object-oriented design
- Test-driven development
- Financial data analysis
- Git version control

---

## Author

Mosa Ndlovu

Melsoft Academy – Python Essentials 2

2026