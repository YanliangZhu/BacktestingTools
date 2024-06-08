import pandas as pd

class WALLET:
    def __init__(self, initial_cash, initial_time='2000-01-01 00:00:00'):
        initial = {
            "Date": [pd.to_datetime(initial_time)],
            "Type": ['Deposit'],
            "Balance": [initial_cash],
            "Holding": [{}]  # format: {ticker: (quantity, average_cost)}
        }
        self.wallet = pd.DataFrame(data=initial)

    # Buy assets
    def buy(self, time, ticker, quantity, price, trading_cost=1):
        wallet = self.wallet.copy()
        cash = wallet["Balance"].iloc[-1]
        holdings = wallet["Holding"].iloc[-1].copy()
        cost = price * quantity + trading_cost
        if cash >= cost:
            new_balance = cash - cost
            if ticker in holdings:
                Q, P = holdings[ticker]
                updated_quantity = Q + quantity
                updated_price = (Q * P + cost) / updated_quantity
                holdings[ticker] = (updated_quantity, updated_price)  # record average price
            else:
                holdings[ticker] = (quantity, cost/quantity)          # record average price
            wallet.loc[len(wallet)] = {
                'Date': pd.to_datetime(time),
                'Type': 'Buy',
                'Balance': new_balance,
                'Holding': holdings
            }
        else:
            print("Insufficient Balance")
        self.wallet = wallet

    # Sell assets
    def sell(self, time, ticker, quantity, price, trading_cost=1):
        wallet = self.wallet.copy()
        cash = wallet["Balance"].iloc[-1]
        holdings = wallet["Holding"].iloc[-1].copy()
        if ticker in holdings:
            Q, P = holdings[ticker]
            if Q >= quantity:
                holdings[ticker] = (Q - quantity, P)
                if Q == quantity:
                    del holdings[ticker]
                proceeds = price * quantity - trading_cost
                new_balance = cash + proceeds
                wallet.loc[len(wallet)] = {
                    'Date': pd.to_datetime(time),
                    'Type': 'Sell',
                    'Balance': new_balance,
                    'Holding': holdings
                }
            else:
                print("Insufficient Holding")
        else:
            print("Ticker not found in holdings")
        self.wallet = wallet
    
    # Return the wallet DataFrame
    def account(self):
        return self.wallet

    # Return the current wallet cash balance
    def balance(self):
        return self.wallet["Balance"].iloc[-1]

    # Return the current wallet holdings
    def holding(self):
        return self.wallet["Holding"].iloc[-1]
