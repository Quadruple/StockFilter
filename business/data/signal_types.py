"""
This module is for defining the signal types that can be produced from the technical indicators.
"""
from enum import Enum


SIGNAL_TYPES = Enum("SIGNAL_TYPES", ["BUY", "SELL", "HOLD"])
