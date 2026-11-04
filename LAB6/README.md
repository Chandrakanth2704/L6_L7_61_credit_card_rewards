# L6_L7_61 — Credit Card Rewards

## Lab 6: Code and Branch Coverage Analysis

### About

This project is a Python-based Credit Card Rewards module developed to demonstrate **Code Coverage and Branch Coverage Analysis using Pytest**.

The application calculates reward points based on credit card tier, spending category, transaction amount, and day of the week. It also calculates late payment fees and determines the health status of a credit card account.

The objective of Lab 6 is to develop additional test cases to achieve at least **90% code coverage and 90% branch coverage** for the application.

### Project Structure

```text
LAB6/
│
├── credit_card_rewards.py
├── test_credit_card_rewards.py
│
├── CodeCoverageTest_credit_card_application.py
├── BranchCoverageTest_credit_card_application.py
│
├── CodeCoverage_Screenshot.png
├── BranchCoverage_Screenshot.png
│
└── .gitignore
```

### Application Features

The `credit_card_rewards.py` module contains three main functions:

| Function | Description |
|---|---|
| `reward_points()` | Calculates reward points based on card tier, spending amount, category, and weekend bonus. |
| `late_payment_fee()` | Calculates late payment fees based on outstanding balance and number of delayed days. |
| `card_status()` | Determines account status based on credit utilisation, missed payments, and frozen status. |

### Testing and Coverage Analysis

Pytest is used to execute test cases, while the `pytest-cov` plugin measures code and branch coverage.

**1. Code Coverage Testing**

File: `CodeCoverageTest_credit_card_application.py`

This file contains additional test cases covering:
- Valid and invalid card tiers.
- Different spending categories.
- Weekend reward bonuses.
- Valid and invalid transaction amounts.
- Different late payment fee conditions.
- Credit card account status conditions and boundaries.

Run the tests:

```bash
pytest -v CodeCoverageTest_credit_card_application.py test_credit_card_rewards.py
```

Generate the code coverage report:

```bash
pytest --cov=credit_card_rewards --cov-report=term-missing CodeCoverageTest_credit_card_application.py test_credit_card_rewards.py
```

**Result: 100% Code Coverage**

- Total statements: 35
- Missed statements: 0
- Tests passed: 32

Screenshot: `CodeCoverage_Screenshot.png`

**2. Branch Coverage Testing**

File: `BranchCoverageTest_credit_card_application.py`

This file contains additional test cases designed to execute different decision outcomes and conditional branches in the application.

Run the branch coverage tests:

```bash
pytest --cov=credit_card_rewards --cov-branch --cov-report=term-missing BranchCoverageTest_credit_card_application.py test_credit_card_rewards.py
```

**Result: 100% Branch Coverage**

- Total statements: 35
- Missed statements: 0
- Total branches: 26
- Partial branches: 0
- Tests passed: 31

Screenshot: `BranchCoverage_Screenshot.png`

### Coverage Summary

| Coverage Metric | Achieved | Required |
|---|---:|---:|
| Code Coverage | 100% | 90% |
| Branch Coverage | 100% | 90% |

Both coverage requirements have been successfully achieved.

### Installation and Execution

**Prerequisites**
- Python 3.x
- Pytest
- pytest-cov

Install the required packages:

```bash
pip install pytest pytest-cov
```

Run all test files:

```bash
pytest -v
```

Run code coverage analysis:

```bash
pytest --cov=credit_card_rewards --cov-report=term-missing
```

Run branch coverage analysis:

```bash
pytest --cov=credit_card_rewards --cov-branch --cov-report=term-missing
```

### Lab 6 Deliverables

The following deliverables are included in the `LAB6` folder:

1. Code coverage test cases.
2. Branch coverage test cases.
3. Terminal screenshot showing code coverage results.
4. Terminal screenshot showing branch coverage results.
5. Coverage analysis demonstrating that both requirements exceed the minimum 90% target.

### Technologies Used

- Python
- Pytest
- pytest-cov
- Git and GitHub

### Repository Structure

All Lab 6 implementation files, test cases, and screenshots are maintained inside the `LAB6` folder. Lab 7 will be added to this repository separately.

---

**Lab 6 Status: Completed**

Code Coverage: **100%**

Branch Coverage: **100%**