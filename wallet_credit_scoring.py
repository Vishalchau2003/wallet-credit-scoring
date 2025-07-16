
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load data
with open('user-wallet-transactions.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Group by userWallet and count action types
wallet_summary = df.groupby('userWallet')['action'].value_counts().unstack(fill_value=0)

# Define scoring logic
def calculate_credit_score(row):
    score = 500  # Base score
    score += row.get('deposit', 0) * 2
    score += row.get('repay', 0) * 5
    score -= row.get('borrow', 0) * 1
    score -= row.get('liquidationcall', 0) * 20
    return max(0, min(1000, score))

wallet_summary['credit_score'] = wallet_summary.apply(calculate_credit_score, axis=1)

# Save credit scores
wallet_summary[['credit_score']].to_csv('wallet_credit_scores.csv')

# Plot distribution for analysis.md
plt.figure(figsize=(10, 6))
plt.hist(wallet_summary['credit_score'], bins=10, edgecolor='black')
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Credit Score Range')
plt.ylabel('Number of Wallets')
plt.grid(True)
plt.savefig('credit_score_distribution.png')
plt.close()

print("Credit scoring completed. Results saved in wallet_credit_scores.csv")
