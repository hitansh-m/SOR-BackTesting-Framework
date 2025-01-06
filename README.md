Smart Order Routing Backtesting Framework

This project implements a backtesting framework for testing execution strategies used in Smart Order Routing (SOR). 
Specifically, it demonstrates the Time-Weighted Average Price (TWAP) strategy. The framework simulates order execution across multiple trading venues using synthetic data and calculates key performance metrics.

Key Features:

Synthetic Data Generation: Generates synthetic price and volume data for testing purposes.
TWAP Execution: Simulates the execution of trades using the TWAP strategy, breaking orders into equal parts over time.
Performance Metrics: Calculates Execution Cost, Slippage, and compares executed trades against a benchmark (VWAP).

Performance Metrics:

Execution Cost: Measures the difference between the executed price and the benchmark price (VWAP).

Slippage: Measures the difference between the expected execution price and the actual fill price.

Outut:

The script will print the benchmark VWAP, average executed price, execution cost, and slippage.
