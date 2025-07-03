# data/collectors/__init__.py
"""
Data collectors package for S&P 500 futures trading system
"""

from .futures_collector import ESFuturesCollector

# Makes imports cleaner
__all__ = ["ESFuturesCollector"]
