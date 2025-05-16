# Black_Scholes_Options_Pricer
A Python project that implements the Black–Scholes model for European option pricing, including calculation of call and put prices, Greeks (delta, gamma, vega, theta, rho), and optional historical volatility estimation using live market data. Additionally, it provides an interactive Streamlit web interface for real‑time inputs and visualization.
🚀 Features

Core Pricing: Compute European call and put option prices via the Black–Scholes formula.

Greeks: Calculate key sensitivities (Δ, Γ, Θ, ν, ρ) for risk management and analysis.


Flexible UIs:

Module (black_scholes.py): Reusable library for integration into other projects or CLI scripts.

Streamlit App (app.py): Interactive dashboard for live parameter inputs, metric display, and volatility auto-fetch.

Testing: Unit tests with pytest to verify formula correctness and edge cases.