# Quantitative Trading System - S&P 500 Futures

Machine learning trading system for ES futures contracts.

## Current Status: v0.2 - Data Collection and Markov Chain calculation
- Real-time ES futures data collection via Yahoo Finance
- OHLCV data with volume validation
- Data quality checks (no-trade detection)
- Fetches 252+ trading days of historical data
- Calculates percentage change between subsequent candles
- Generates a probability matrix for a given array of percentage changes
- Normal distribution bin packing to decide states

## Sample Output for v0.1
Fetched 252 rows of data

Date range: 2024-07-02 00:00:00-04:00 to 2025-07-02 00:00:00-04:00

Date                      Open      High      Low       Close     Volume    Dividends Stock Splits

2024-07-02 00:00:00-04:00 5533.50  5569.75  5502.75  5568.75  1315097      0.0        0.0

2024-07-03 00:00:00-04:00 5563.75  5595.75  5559.75  5590.25   808966      0.0        0.0

2024-07-05 00:00:00-04:00 5591.00  5626.00  5585.00  5621.50  1233173      0.0        0.0

2024-07-08 00:00:00-04:00 5612.00  5637.50  5610.75  5625.25   981186      0.0        0.0

2024-07-09 00:00:00-04:00 5627.75  5645.75  5626.25  5631.25  1063568      0.0        0.0

## Sample Output for v0.2
Probability Matrix created
(array([[0.09090909, 0.19393939, 0.25454545, 0.28484848, 0.11515152,
        0.06060606],
       [0.04651163, 0.12522361, 0.24150268, 0.43649374, 0.11091234,
        0.03935599],
       [0.01723264, 0.07754688, 0.30917385, 0.50177395, 0.07704004,
        0.01723264],
       [0.01586754, 0.06864436, 0.35046568, 0.47844084, 0.07140393,
        0.01517765],
       [0.04798464, 0.15163148, 0.26871401, 0.36852207, 0.10556622,
        0.05758157],
       [0.11949686, 0.16352201, 0.19496855, 0.23899371, 0.16352201,
        0.11949686]]), np.int64(2), np.float64(-0.00023135612409891493), np.float64(0.015371414162231407))

## Next Version: v0.3
- Multi-timeframe analysis
- Real-time execution
- Risk management
- Trade bias

## Project Timeline
- Database storage system
- ML price prediction models
- Backtesting engine
- Performance analytics
