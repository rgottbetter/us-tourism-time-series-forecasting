import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the data from Excel
filename = r'monthlyvisitors.xlsx'
data = pd.read_excel(filename)

# Extract the time series data
time_series = data['Visitors']

# Convert the date strings to datetime format
dates = data['Month']

# Convert to a datetime array
dates = pd.to_datetime(dates)

# Starting parameters for ARMA, ARIMA, and SARIMA models
arma_start_params = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
arima_start_params = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
sarima_start_params = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# ARMA(3,4) Model
armaModel = ARIMA(time_series, order=(3, 0, 4), trend='n')
fitARMA = armaModel.fit(start_params=arma_start_params)
forecastARMA = fitARMA.get_forecast(steps=10)

# ARIMA(3,2,4) Model
arimaModel = ARIMA(time_series, order=(3, 2, 4), trend='n')
fitARIMA = arimaModel.fit(start_params=arima_start_params)
forecastARIMA = fitARIMA.get_forecast(steps=10)

# SARIMA(3,2,4)x(3,2,2)12 Model
sarimaModel = ARIMA(time_series, order=(3, 2, 4), seasonal_order=(3, 2, 2, 12), trend='n')
fitSARIMA = sarimaModel.fit(start_params=sarima_start_params)
forecastSARIMA = fitSARIMA.get_forecast(steps=10)

# Plot the forecasts
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(dates, time_series, 'r', label='Original Data')
plt.plot(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastARMA.predicted_mean, 'g', label='ARMA Forecast')
plt.fill_between(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastARMA.conf_int().iloc[:, 0], forecastARMA.conf_int().iloc[:, 1], color='green', alpha=0.2)
plt.title('ARMA Forecast')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(dates, time_series, 'r', label='Original Data')
plt.plot(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastARIMA.predicted_mean, 'g', label='ARIMA Forecast')
plt.fill_between(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastARIMA.conf_int().iloc[:, 0], forecastARIMA.conf_int().iloc[:, 1], color='green', alpha=0.2)
plt.title('ARIMA Forecast')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(dates, time_series, 'r', label='Original Data')
plt.plot(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastSARIMA.predicted_mean, 'g', label='SARIMA Forecast')
plt.fill_between(pd.date_range(start=dates.iloc[-1], periods=10, freq='M'), forecastSARIMA.conf_int().iloc[:, 0], forecastSARIMA.conf_int().iloc[:, 1], color='green', alpha=0.2)
plt.title('SARIMA Forecast')
plt.legend()

plt.show()
