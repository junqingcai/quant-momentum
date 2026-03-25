# Momentum-Based Multi-Asset Strategy

## 📌 Overview

This project implements a quantitative trading strategy based on momentum and multi-asset portfolio allocation. The strategy dynamically allocates capital across different asset classes to capture medium-term trends while maintaining diversification.

---

## 🧠 Strategy Logic

* **Asset Universe**: Non-ferrous metals, gold, silver, and healthcare ETFs
* **Core Factor**: 20-day momentum (return-based ranking)
* **Selection Rule**: Allocate capital to top-performing assets
* **Rebalancing Frequency**: Monthly
* **Risk Control**: Shift to defensive assets (e.g., gold) when all assets show weak momentum

---

## ⚙️ Implementation

* **Platform**: JoinQuant
* **Language**: Python
* **Key Components**:

  * Historical data retrieval
  * Momentum signal calculation
  * Portfolio rebalancing

---

## 📊 Backtest Results

### 📈 Equity Curve & Benchmark Comparison

![Equity Curve](result1.png)

The strategy shows strong cumulative returns and consistently outperforms the benchmark (CSI 300), especially during trending market periods.

---

### 📊 Daily Profit & Trading Activity

![Performance Metrics](result2.png)

The profit distribution indicates:

* Frequent small gains
* Occasional larger drawdowns
* Active rebalancing behavior over time

---

## 📉 Performance Summary

* **Annual Return**: 98.25%
* **Excess Return**: 70.15%
* **Sharpe Ratio**: 2.706
* **Max Drawdown**: 31.83%
* **Win Rate**: 81.8%

The strategy achieves high returns and strong risk-adjusted performance, but exhibits noticeable drawdowns during market reversals.

---

## ⚠️ Limitations

* High concentration in cyclical assets (e.g., metals)
* Drawdown risk during trend reversals
* Limited diversification and correlation control

---

## 🚀 Future Improvements

* Introduce correlation-based portfolio optimization (e.g., risk parity)
* Add volatility control mechanisms
* Improve drawdown management
* Test robustness across different market regimes

---

## 📁 Project Structure

* `strategy.py`: trading strategy implementation
* `result1.png`: equity curve and benchmark comparison
* `result2.png`: daily profit and trading activity

---

## 📬 Notes

This project serves as an exploratory study of momentum-based asset allocation strategies. Future work will focus on improving robustness, risk control, and real-world applicability.
