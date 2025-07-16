# Wallet Credit Scoring — Aave V2 Protocol

## Problem Statement

We are required to develop a machine learning model that assigns a credit score between 0–1000 to each wallet based on transaction data from the Aave V2 protocol. The scoring reflects wallet behavior: higher scores represent safer, more reliable wallets, and lower scores reflect risky or exploitative behavior.

---

## Approach

### Features Engineered
- **Total deposits**: Indicates active participation.
- **Total borrows**: Higher borrow counts may indicate risk.
- **Total repays**: Reflects responsible behavior.
- **Total liquidation calls**: High risk, penalized in scoring.

### Scoring Logic
- **Base score**: 500 points.
- **+2 points** per deposit.
- **+5 points** per repay.
- **-1 point** per borrow.
- **-20 points** per liquidationcall.
- Score capped between **0 and 1000**.

---

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib
