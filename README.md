# Backtesting Tools: WALLET Class
This repository contains the implementation of a `WALLET` class for managing a simple trading wallet.

## Usage

```python
import pandas as pd
from wallet import WALLET

# Initialize the wallet with initial cash
wallet = WALLET(1000)

# Buy some assets
wallet.buy('2024-06-08 12:00:00', 'AAPL', 5, 150)

# Sell some assets
wallet.sell('2024-06-09 12:00:00', 'AAPL', 2, 160)

# Print account details
print(wallet.account())

# Print current balance
print(wallet.balance())

# Print current holdings
print(wallet.holding())
