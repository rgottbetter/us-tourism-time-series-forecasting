# us-tourism-time-series-forecasting

Forecasting International Tourist Visits to the United States

Overview:

This project forecasts monthly international tourist arrivals to the United States using classical time series modeling techniques. The objective was to identify an appropriate statistical model capable of capturing both trend and seasonal behavior in inbound tourism data and to evaluate forecasting performance on out-of-sample observations.

The project was completed as part of EN.625.695 – Time Series Analysis at Johns Hopkins University.

This repository contains the model section, forecasting, and model implementation portion of the group project, focusing on ARMA, ARIMA, and SARIMA model evaluation and forecasting.

Objective:
Model monthly inbound tourism data from 1996–2023
Compare ARMA, ARIMA, and SARIMA time series models
Evaluate forecasting performance using RMSE and MAPE
Generate short-term forecasts for inbound tourism demand

Data:
The dataset consists of monthly international tourist arrivals to the United States(original source: National Travel and Tourism Office).
The series exhibits:
Long-term upward trend
Strong seasonal patterns
Structural disruption during COVID-19
These characteristics motivated the use of seasonal time series models.

Methodology:
Model Evaluation
The following models were tested:
ARMA
ARIMA
SARIMA

Model parameters were selected using:
Akaike Information Criterion (AIC)
Bayesian Information Criterion (BIC)

Forecast performance was evaluated using:
Root Mean Squared Error (RMSE)
Mean Absolute Percentage Error (MAPE)

Results:

The SARIMA(3,2,4) × (3,2,2)₁₂ model provided the best overall fit and forecasting performance, capturing both trend and seasonal structure present in the data.
The model demonstrated improved out-of-sample forecasting accuracy compared to ARMA and ARIMA alternatives.
