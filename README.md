# Simple Banking System Simulator (Python CLI)

A lightweight, console-based banking application written in Python. The project simulates a multi-user login gateway followed by an interactive automated teller machine (ATM) environment allowing balance checks, deposits, and withdrawals.

## Features

- **Multi-User Authentication:** Secure login simulation supporting distinct user accounts with static credentials.
- **Stateful Transaction Loop:** An active command-line session that updates and preserves the account balance throughout the program execution window.
- **ATM Operations:**
  - **Deposit:** Adds funds instantly to the core balance.
  - **Withdrawal:** Deducts funds from the active balance.
  - **Balance Inquiry:** Displays real-time current ledger funds.
- **Graceful Termination:** Standardized exit routine to break operational loops cleanly.

## Account Test Credentials

For testing purposes, you can log in using any of the following pre-configured user credentials:

| Username | Password |
| :--- | :--- |
| priya | 1234 |
| rajnesh | 5678 |
| tushar | 1111 |

## Getting Started

### Prerequisites
- Python 3.x installed on your environment.

### Execution
1. Clone the repository or download the script file.
2. Open a terminal windows inside the script directory.
3. Launch the application:
   ```bash
   python banking_system.py
