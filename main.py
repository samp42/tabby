import tabby
import sys
import os

sys.path.append(os.path.abspath("."))

tabby.read_csv("./datasets/hourly-weather-surface-brazil-southeast-region/north.csv")
