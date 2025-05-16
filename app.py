import streamlit as st
from black_scholes import black_scholes_call, black_scholes_put
import yfinance as yf
import numpy as np

# Title
st.title("Black–Scholes Options Calculator")

# User inputs for option parameters
S = st.number_input("Spot Price (S)", value=100.0)
K = st.number_input("Strike (K)",    value=100.0)
T = st.number_input("Time to Expiry (yrs)", value=0.5)
r = st.number_input("Risk-free Rate",    value=0.01)
sigma = st.number_input("Volatility (σ)", value=0.2)

#Calculate option prices using Black-Scholes
call_price = black_scholes_call(S, K, T, r, sigma)
put_price  = black_scholes_put(S, K, T, r, sigma)

# Displays calculated option prices
st.metric("Call Price", f"${call_price:0.2f}")
st.metric("Put  Price", f"${put_price:0.2f}")

# Gather 1 year of historical closing prices example
data = yf.Ticker("AAPL").history(period="1y")["Close"]

# Calculate daily log returns
rets = np.log(data / data.shift(1)).dropna()

# Calculate annualized historical volatility
hist_vol = rets.std() * np.sqrt(252)
