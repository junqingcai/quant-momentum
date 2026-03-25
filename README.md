# Momentum-Based Multi-Asset Strategy

##  Overview

This project implements a quantitative trading strategy based on momentum and multi-asset portfolio allocation.
The strategy dynamically allocates capital among different asset classes to capture market trends while maintaining diversification.

---

##  Strategy Logic

* **Asset Universe**: Non-ferrous metals, gold, silver, and healthcare ETFs
* **Factor**: 20-day momentum
* **Selection Rule**: Select top-performing assets based on recent returns
* **Rebalancing Frequency**: Monthly
* **Risk Control**: Shift to gold when all assets exhibit negative momentum

---

##  Implementation

* **Platform**: JoinQuant
* **Language**: Python
* **Core Components**:

  * Historical price data retrieval
  * Momentum calculation
  * Portfolio rebalancing

---

##  Backtest Results

###  Equity Curve

![Equity Curve](equity_curve.png)

###  Performance Metrics

![Performance Metrics](metrics.png)

---

##  Performance Summary

* **Annual Return**: 98.25%
* **Max Drawdown**: 31.83%
* **Sharpe Ratio**: 2.70

The strategy significantly outperforms the benchmark. However, it also exhibits relatively high volatility and drawdown, indicating the need for improved risk management.

---

##  Limitations

* High exposure to cyclical assets (e.g., non-ferrous metals)
* Limited diversification due to asset correlation
* Simple risk control mechanism

---

##  Future Improvements

* Introduce correlation-based portfolio construction
* Apply risk parity or volatility targeting
* Improve drawdown control
* Test robustness across different market conditions

---

##  Project Structure

* `strategy.py`: trading strategy implementation
* `result1.png`: cumulative return curve
* `result2.png`: backtest performance metrics

---

##  Notes

This project is a preliminary exploration of quantitative investment strategies, focusing on momentum-based asset allocation. Further improvements are needed to enhance robustness and real-world applicability.
