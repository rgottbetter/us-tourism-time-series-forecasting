import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import itertools
from tqdm import tqdm
import warnings

warnings.filterwarnings('ignore')

#update your file path
data = pd.read_excel(r'US tourist arrival dataset.xlsx', sheet_name='US Tourist')

df = pd.DataFrame(data, columns=['Select this link and click Refresh/Edit Download to update data and add or remove series','Visitor Arrivals'])
df.columns = ['Month', 'Visitors']
tourists = df.drop(index=[0,1,2,3,335], axis=0)
tourists = tourists.reset_index(drop=True)
tourists.set_index('Month', inplace=True)


tourists['Visitors-log'] = np.log(tourists['Visitors'].astype(float))
tourists['Visitors-station'] = tourists['Visitors-log'].diff(3)
tourists = tourists.dropna()


fig, ax = plt.subplots(3, figsize=(15,10))
ax[0].plot(tourists['Visitors'])
ax[0].set_title(['US Tourists'])
ax[1].plot(tourists['Visitors-log'])
ax[1].set_title(['Visitors after Log Transformation'])
ax[2].plot(tourists['Visitors-station'])
ax[2].set_title('Cloase after Differecing')

#plot_acf(tourists['Visitors'], lags=50)
#plot_pacf(tourists['Visitors'], lags=50)

plot_acf(tourists['Visitors-station'], lags=50)
plot_pacf(tourists['Visitors-station'], lags=50)

plt.show()
ARMAaic = []
ARMAparams = []
# ARMA
# optimal_parameter p,q
p = range(0,4)
q = range(0,5)
d = range(0,1)
pq = list(itertools.product(p,d,q))
with tqdm(total=len(pq)) as pg:
    for i in pq:
        pg.update(1)
        try:
            ARMAmodel = ARIMA(tourists['Visitors'].astype(float), order=(i)).fit()
            ARMAaic.append(round(ARMAmodel.aic, 2))
            ARMAparams.append((i))
        except:
            continue

ARMAoptimal = [(ARMAparams[i],j) for i,j in enumerate(ARMAaic) if j == min(ARMAaic)]
arma_model = ARIMA(tourists['Visitors'].astype(float), order = ARMAoptimal[0][0], freq='MS').fit()



#ARIMA
#optimal parameter p, d, q

p = range(0, 4)
d = range(0, 3)
q = range(0, 5)

pdq = list(itertools.product(p,d,q))

ARIMAaic = []
ARIMAparams = []

with tqdm(total=len(pdq)) as pg:
    for i in pdq:
        pg.update(1)
        try:
            ARIMAmodel = ARIMA(tourists['Visitors'].astype(float), order=(i)).fit()
            ARIMAaic.append(round(ARIMAmodel.aic, 2))
            ARIMAparams.append((i))
        except:
            continue 

ARIMAoptimal = [(ARIMAparams[i],j) for i,j in enumerate(aic) if j == min(aic)]


arima_model = ARIMA(tourists['Visitors'].astype(float), order=ARIMAoptimal[0][0], freq='MS').fit()
forecast = arima_model.forecast(steps=20)


#SARIMA
p = range(2, 4)
d = range(1, 3)
q = range(2, 5)
t = ['t']
P = range(2, 4)
D = range(1, 3)
Q = range(2, 5)
m = [0,12]



pdqtPDQm = list(itertools.product(p,d,q,t,P,D,Q,m))

SARIMAaic = []
SARIMAparams = []

with tqdm(total=len(pdqtPDQm)) as pg:
    for i in pdqtPDQm:
        pg.update(1)
        try:
            SARIMAmodel = SARIMAX(tourists['Visitors'].astype(float), order=(i[0:3]), seasonal_order=(i[4:8]),
                                  trend=(i[3])).fit()
            SARIMAaic.append(round(SARIMAmodel.aic, 2))
            SARIMAparams.append((i))
        except:
            continue

SARIMAoptimal = [(SARIMAparams[i],j) for i,j in enumerate(SARIMAaic) if j == min(SARIMAaic)]
sarima_model = SARIMAX(tourists['Visitors'].astype(float), order=(SARIMAoptimal[0][0][0:3]), seasonal_order=(SARIMAoptimal[0][0][4:8]),
                                  trend=(SARIMAoptimal[0][0][3]), freq='MS').fit()
#arima.summary()









arima_model = ARIMA(tourists['Visitors'].astype(float), order=optimal[0][0], freq='MS').fit()
forecast = arima_model.forecast(steps=20)










fig, ax = plt.subplots(1, 1)
fig.set_size_inches(10, 5)
fig.set_dpi(300)
ax.plot(tourists['Visitors'], color='green', label='real')
ax.plot(forecast, color='red', label='prediction')
plt.show()

# Fit the models before plotting
arma_model = ARIMA(tourists['Visitors'].astype(float), order=ARMAoptimal[0][0], freq='MS').fit()
arima_model = ARIMA(tourists['Visitors'].astype(float), order=ARIMAoptimal[0][0], freq='MS').fit()
sarima_model = SARIMAX(tourists['Visitors'].astype(float), order=(SARIMAoptimal[0][0][0:3]), 
                       seasonal_order=(SARIMAoptimal[0][0][4:8]), trend=(SARIMAoptimal[0][0][3]), freq='MS').fit()

# ARMA Forecast
arma_forecast = arma_model.forecast(steps=24)

# ARIMA Forecast
arima_forecast = arima_model.forecast(steps=24)

# SARIMA Forecast
sarima_forecast = sarima_model.get_forecast(steps=24)

# Assuming your original time series data is stored in a variable named 'data'
# You can create a time index for the next 24 months
forecast_index = pd.date_range(start=tourists.index[-1], periods=25, freq='M')[1:]

# Plotting the original data
plt.plot(tourists['Visitors'], label='Original Data')

# Plotting ARMA forecast
plt.plot(forecast_index, arma_forecast, label='ARMA Forecast')

# Plotting ARIMA forecast
plt.plot(forecast_index, arima_forecast, label='ARIMA Forecast')

# Plotting SARIMA forecast
plt.plot(forecast_index, sarima_forecast.predicted_mean, label='SARIMA Forecast')

plt.legend()
plt.show()

