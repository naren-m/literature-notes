# The Three Bucket Strategy for Sustainable Cash Flow

---

## The Core Problem

You need regular cash flow—for EMIs, living expenses, or any recurring obligation. Your investments don't give steady returns. Some years the market gives 20%. Some years it falls 30%.

If you withdraw money during a bad year, you sell at a loss. Do this repeatedly, and your corpus depletes faster than planned.

This is called **sequence of returns risk**.

---

## The Solution: Separate Money by Time Horizon

Instead of one big corpus, split your money into three buckets based on when you need it:

Bucket 1: Stability, Cash Flow, and Safety
- Liquid funds, Money market funds, Ultra-short-term, Short-term debt funds (Corporate bond funds, Credit risk funds)
- Maintains 3 years of withdrawal to prevent panic and protects SWP during market crashes

Bucket 2: Income and refilling Bucket 1 with stable low volatility returns
- Intermediate (Refills Bucket 1 every year)
- Conservative hybrid funds, Equity savings fund, Low volatility variants of Balance Advantage Funds, Short duration funds, Multi-asset funds
- The core 'ISR Bucket' that creates stable low volatility returns to refill safety buckets

Bucket 3: Growth, Refill Bucket 2
- Flexi cap, Mid cap, Index funds
- Grows wealth and beats inflation. Refills Bucket 2 every few years

| Bucket   | When You Need It | What It Does            |
| -------- | ---------------- | ----------------------- |
| Bucket 1 | Now (0-3 years)  | Fund your cash flow     |
| Bucket 2 | Soon (3-7 years) | Refill Bucket 1         |
| Bucket 3 | Later (7+ years) | Grow and beat inflation |

```mermaid
flowchart LR
    B3["BUCKET 3<br/>Growth<br/>7+ years"] -->|"Refill every 3-5 years"| B2["BUCKET 2<br/>Income<br/>3-7 years"]
    B2 -->|"Refill yearly"| B1["BUCKET 1<br/>Stability<br/>0-3 years"]
    B1 -->|"Monthly"| OUT["Cash Flow<br/>(EMI / Expenses)"]
```

---

## How Much Do You Need?

Use this formula:

```
Corpus = Monthly Cash Flow × 12 × ISR
```

**ISR (Income Stability Ratio)** is a multiplier based on your goal duration:

| Goal Type                        | Duration    | ISR   | Example              |
| -------------------------------- | ----------- | ----- | -------------------- |
| Indefinite (wealth preservation) | Forever     | 17.5  | Passive income       |
| Long-term (loan payoff)          | 15-20 years | 10-12 | Home loan EMI        |
| Medium-term                      | 10-15 years | 8-10  | Education fund       |
| Short-term                       | 5-10 years  | 5-7   | Car loan, renovation |

### Examples

| Monthly Need | Goal             | ISR  | Corpus Required |
| ------------ | ---------------- | ---- | --------------- |
| ₹50,000      | Passive income   | 17.5 | ₹1.05 Crore     |
| ₹50,000      | 15-year loan EMI | 12   | ₹72 Lakhs       |
| ₹1,00,000    | Passive income   | 17.5 | ₹2.10 Crore     |
| ₹1,00,000    | 15-year loan EMI | 12   | ₹1.44 Crore     |

---

## The Three Buckets Explained

### Bucket 1: Stability (33% of corpus)

**Purpose:** Fund cash flow for the next 3 years, regardless of market conditions.

**Investments:** Liquid funds, money market funds, short-term debt, FDs.

**Expected return:** 6-7%

**Rule:** Never runs dry. Gets refilled from Bucket 2.

---

### Bucket 2: Income (33% of corpus)

**Purpose:** Generate stable returns. Refill Bucket 1 every year.

**Investments:** Equity savings funds, conservative hybrid, balanced advantage funds.

**Expected return:** 8-10%

**Rule:** Low volatility. This is your buffer zone.

---

### Bucket 3: Growth (33% of corpus)

**Purpose:** Beat inflation. Refill Bucket 2 every few years.

**Investments:** Flexi cap, mid cap, index funds.

**Expected return:** 12-15%

**Rule:** Never touch during a crash. Let it recover first.

---

## How Money Flows

```mermaid
flowchart TB
    subgraph GOOD["GOOD YEARS"]
        G3["Bucket 3<br/>Growth"] --harvest gains--> G2["Bucket 2<br/>Income"]
        G2["Bucket 2<br/>Income"] --move returns--> G1["Bucket 1<br/>Stability"]

    end
    
    subgraph BAD["BAD YEARS"]
        B3["Bucket 3: Don't sell"]
        B2["Bucket 2: Don't sell"]
        B1["Bucket 1: Keep withdrawing"]
        B3  -.->|"Wait"| B2
        B2  -.->|"Wait"| B1
    end
    G1 --> W1["💰 Withdrawals Continue"]
    B1 --> W2["💰 Withdrawals Continue"]
```

**Good years:** Harvest gains from higher buckets, move down.

**Bad years:** Don't sell. Bucket 1 has 3 years of buffer. Wait for recovery.

---

## When to Move Money

| Trigger                        | Action                    |
| ------------------------------ | ------------------------- |
| Bucket 1 < 1 year of cash flow | Refill from Bucket 2      |
| Bucket 2 < 3 years runway      | Refill from Bucket 3      |
| Bucket 3 up >15% in a year     | Harvest gains to Bucket 2 |
| Market crash                   | Do nothing. Wait.         |

```mermaid
flowchart TB
    START["Start of Year"] --> Q1{"Bucket 1 < 1 year?"}
    Q1 -->|Yes| Q2{"Bucket 2 has gains?"}
    Q1 -->|No| DONE["No action needed"]
    Q2 -->|Yes| A1["Move B2 → B1"]
    Q2 -->|No| Q3{"Bucket 3 has gains?"}
    Q3 -->|Yes| A2["Move B3 → B2 → B1"]
    Q3 -->|No| WAIT["Wait for recovery"]
```

---

## 15-Year Simulation: Paying Off a Loan

₹3.5 Cr corpus, ₹50L annual EMI:

```text
YEAR    BUCKET 1        BUCKET 2        BUCKET 3        TOTAL       EMI PAID
────────────────────────────────────────────────────────────────────────────
  0     ₹1.20 Cr        ₹1.20 Cr        ₹1.10 Cr       ₹3.50 Cr      ₹0
        [████████]      [████████]      [███████]
        
  1     ₹0.75 Cr        ₹1.30 Cr        ₹1.25 Cr       ₹3.30 Cr      ₹50L
        [█████]         [████████]      [████████]
        ▲ paid ₹50L     ▲ grew 8%       ▲ grew 14%
        
  2     ₹0.30 Cr        ₹1.40 Cr        ₹1.43 Cr       ₹3.13 Cr      ₹1.0 Cr
        [██]            [█████████]     [█████████]
        ▲ running low
        
  3     ₹0.90 Cr ◄──────₹1.00 Cr        ₹1.63 Cr       ₹3.53 Cr      ₹1.5 Cr
        [██████]  REFILL [██████]       [██████████]
        
  5     ₹0.40 Cr        ₹1.20 Cr ◄──────₹1.50 Cr       ₹3.10 Cr      ₹2.5 Cr
        [███]           [████████]REFILL[█████████]
        
  7     ₹0.85 Cr ◄──────₹0.95 Cr        ₹1.80 Cr       ₹3.60 Cr      ₹3.5 Cr
        [█████]  REFILL [██████]        [███████████]
        
```

**Result:** ₹7.5 Cr paid out over 15 years. ₹90L corpus remaining.

---

## How Long Money Sits in Each Bucket

| Bucket   | Duration    | Why                   |
| -------- | ----------- | --------------------- |
| Bucket 1 | 1-3 years   | Gets spent monthly    |
| Bucket 2 | 3-7 years   | Waits to refill B1    |
| Bucket 3 | 7-15+ years | Grows until harvested |


```text
🍇 GRAPES (New Money)     →  Put in BUCKET 3 (cellar)
   Age for 10+ years
   
🍷 YOUNG WINE             →  Move to BUCKET 2 (cabinet)  
   Age for 3-5 years
   
🥂 READY TO DRINK         →  Move to BUCKET 1 (table)
   Consume within 1-3 years
```

---

## Stress Test: March 2020 Crash

What happens when markets fall 35%?

| Date     | Bucket 1 | Bucket 2 | Bucket 3 | Action             |
| -------- | -------- | -------- | -------- | ------------------ |
| Jan 2020 | ₹1.20 Cr | ₹1.20 Cr | ₹1.10 Cr | Normal             |
| Mar 2020 | ₹1.15 Cr | ₹1.00 Cr | ₹0.72 Cr | Crash. Don't sell. |
| Dec 2020 | ₹0.70 Cr | ₹1.20 Cr | ₹1.10 Cr | Recovered.         |
| Mar 2021 | ₹0.65 Cr | ₹1.30 Cr | ₹1.30 Cr | Harvest B3 gains.  |

You never sold at the bottom. Bucket 1 had enough buffer to wait.

---

## Handling Increasing Costs

If your cash flow needs grow 6% yearly:

| Year | Monthly Need |
| ---- | ------------ |
| 1    | ₹1,00,000    |
| 5    | ₹1,26,248    |
| 10   | ₹1,68,948    |
| 20   | ₹3,02,560    |

Bucket 3 (equity) grows faster than 6%. It funds the increasing withdrawals.

For fixed obligations like loan EMIs, this isn't needed—EMI stays constant.

---

## Investment Options

### Bucket 1 (Stability)

**India:** HDFC Liquid, ICICI Money Market, Axis Short Term, Bank FD

**US:** SGOV, VGSH, Money Market (SPAXX), T-Bills

---

### Bucket 2 (Income)

**India:** ICICI Equity Savings, HDFC Balanced Advantage, ICICI Multi-Asset

**US:** SCHD, VBIAX, JEPI, AOK

---

### Bucket 3 (Growth)

**India:** Parag Parikh Flexi Cap, Mirae Large & Midcap, UTI Nifty 50 Index

**US:** VTI, VOO, QQQ, VGT

---

## Adapting ISR for Your Goal

| If your goal is...     | Use ISR | Corpus can...   |
| ---------------------- | ------- | --------------- |
| Passive income forever | 17.5    | Never deplete   |
| 20-year loan payoff    | 10-12   | Deplete to zero |
| 15-year loan payoff    | 8-10    | Deplete to zero |
| 10-year goal           | 6-8     | Deplete to zero |

Lower ISR = smaller corpus needed, but corpus depletes over time.

Higher ISR = larger corpus needed, but corpus sustains indefinitely.

---

## Summary

1. **Split corpus into 3 buckets** by time horizon
2. **Bucket 1** funds cash flow (3 years buffer)
3. **Bucket 2** refills Bucket 1 (stable returns)
4. **Bucket 3** grows wealth (long-term compounding)
5. **Never sell Bucket 3 during crashes**
6. **Harvest gains in good years**, move down the chain

The system ensures you never sell at the wrong time.

---

## Quick Reference

**Corpus formula:**
```
Monthly Need × 12 × ISR = Required Corpus
```

**ISR by goal:**
```
Indefinite income: 17.5
15-20 year goal:   10-12
10-15 year goal:   8-10
5-10 year goal:    5-7
```

**Allocation:**
```
Bucket 1: 33% (Debt)
Bucket 2: 33% (Hybrid)  
Bucket 3: 33% (Equity)
```

**Refill rules:**
```
B2 → B1: Every 1-2 years
B3 → B2: Every 3-5 years
During crash: Do nothing
```

---

*This is an educational article. Consult a financial advisor before investing.*
