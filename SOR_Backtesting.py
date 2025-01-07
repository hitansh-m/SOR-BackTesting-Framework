import numpy as np
import pandas as pd

def generate_synthetic_data(num_points=60):
    """
    Generate synthetic price and volume data for demonstration.
    """
    np.random.seed(42)
    timestamps = pd.date_range(start='2021-01-01', periods=num_points, freq='min')
    prices = np.cumsum(np.random.normal(0, 0.1, num_points)) + 100  
    volumes = np.random.randint(50, 200, size=num_points)           
    return pd.DataFrame({'timestamp': timestamps,
                         'price': prices,
                         'volume': volumes})

def compute_vwap(data):
    total_volume = (data['price'] * data['volume']).sum()
    sum_volume = data['volume'].sum()
    return total_volume / sum_volume

def twap_execution(data, total_shares=100, start_idx=0, end_idx=59):
    slices = end_idx - start_idx + 1
    shares_per_slice = total_shares // slices

    executed_prices = []
    expected_prices = []

    for i in range(start_idx, end_idx + 1):
        current_price = data.loc[i, 'price']
        expected_prices.append(current_price)

        actual_fill_price = current_price + np.random.normal(0, 0.02)
        executed_prices.append(actual_fill_price)

    return executed_prices, expected_prices

if __name__ == "__main__":
    data = generate_synthetic_data(num_points=60)
    data_vwap = compute_vwap(data)

    executed_prices, expected_prices = twap_execution(data, total_shares=100)

    avg_executed_price = np.mean(executed_prices)
    execution_cost = avg_executed_price - data_vwap

    avg_expected_price = np.mean(expected_prices)
    slippage = avg_executed_price - avg_expected_price

    # Output results
    print(f"Global VWAP (benchmark): {data_vwap:.4f}")
    print(f"Average Executed Price: {avg_executed_price:.4f}")
    print(f"Execution Cost vs VWAP: {execution_cost:.4f}")
    print(f"Slippage (Expected vs Actual): {slippage:.4f}")
