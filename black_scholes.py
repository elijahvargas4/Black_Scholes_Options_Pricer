import numpy as np
from scipy.stats import norm
import yfinance as yf

# S: spot price, K: strike price, T: time to maturity (years)
# r: risk-free rate, sigma: volatility

# Calculate d1
def d1(S, K, T, r, sigma):
    return (np.log(S/K)) + ((r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

# Calculate d2
def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - (sigma * np.sqrt(T))

# Calculate the Black-Scholes price for a European call option
# S * N(D1) - K * exp(-rT) * N(D2)
def black_scholes_call(S, K, T, r, sigma):
    D1, D2 = d1(S, K, T, r, sigma), d2(S, K, T, r, sigma)
    return (S * norm.cdf(D1)) - ((K * np.exp(-r*T)) * (norm.cdf(D2)))

# Calculate the Black-Scholes price for a European put option
# K * exp(-rT) * N(-D2) - S * N(-D1)
def black_scholes_put(S, K, T, r, sigma):
    D1, D2 = d1(S, K, T, r, sigma), d2(S, K, T, r, sigma)
    return (K * np.exp(-r*T) * norm.cdf(-D2)) - (S * norm.cdf(-D1))

# Calculate the delta of a call option
def delta_call(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))

# Calculate the delta of a put option
def delta_put(S, K, T, r, sigma):
    return delta_call(S, K, T, r, sigma) - 1