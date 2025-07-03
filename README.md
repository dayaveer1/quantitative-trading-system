# Quantitative Trading System - S&P 500 Futures

Machine learning trading system for ES futures contracts.

## Current Status: v0.1 - Data Collection
- Real-time ES futures data collection via Yahoo Finance
- OHLCV data with volume validation
- Data quality checks (no-trade detection)
- Fetches 252+ trading days of historical data

## Sample Output
Fetched 252 rows of data

Date range: 2024-07-02 00:00:00-04:00 to 2025-07-02 00:00:00-04:00

Date                      Open      High      Low       Close     Volume    Dividends Stock Splits
2024-07-02 00:00:00-04:00 5533.50  5569.75  5502.75  5568.75  1315097      0.0        0.0
2024-07-03 00:00:00-04:00 5563.75  5595.75  5559.75  5590.25   808966      0.0        0.0
2024-07-05 00:00:00-04:00 5591.00  5626.00  5585.00  5621.50  1233173      0.0        0.0
2024-07-08 00:00:00-04:00 5612.00  5637.50  5610.75  5625.25   981186      0.0        0.0
2024-07-09 00:00:00-04:00 5627.75  5645.75  5626.25  5631.25  1063568      0.0        0.0

Current ES price: $6275.50

## Next Version: v0.2
- Database storage system
- Technical indicators (RSI, MACD, Bollinger Bands)

## Project Timeline
- ML price prediction models
- Risk management framework
- Backtesting engine
- Performance analytics
