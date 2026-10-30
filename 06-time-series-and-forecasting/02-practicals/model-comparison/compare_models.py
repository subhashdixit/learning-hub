"""Compare real fitted forecasting implementations on one synthetic temporal holdout.

Run in a dedicated environment with requirements.txt. No remote data or API key.
This is a development comparison, not proof one family always wins.
"""
from pathlib import Path
import json, warnings
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet

rng=np.random.default_rng(42)
n=280; horizon=28;t=np.arange(n)
promotion=((t%31)<3).astype(float)
y=20+.05*t+4*np.sin(2*np.pi*t/7)+2*promotion+rng.normal(0,.5,n)
dates=pd.date_range('2024-01-01',periods=n,freq='D')
cut=n-horizon;train=y[:cut];actual=y[cut:]
exog=np.column_stack([t/n,promotion])
predictions={'seasonal_naive':np.resize(train[-7:],horizon)}
predictions['ARIMA']=np.asarray(ARIMA(train,order=(2,1,1)).fit().forecast(horizon))
predictions['SARIMA']=np.asarray(SARIMAX(train,order=(1,1,0),seasonal_order=(1,0,0,7),enforce_stationarity=False).fit(disp=False,maxiter=200).forecast(horizon))
predictions['SARIMAX']=np.asarray(SARIMAX(train,exog=exog[:cut],order=(1,0,0),seasonal_order=(1,0,0,7),trend='c',enforce_stationarity=False).fit(disp=False,maxiter=300).forecast(horizon,exog=exog[cut:]))
predictions['ETS_Holt_Winters']=np.asarray(ExponentialSmoothing(train,trend='add',seasonal='add',seasonal_periods=7,initialization_method='estimated').fit().forecast(horizon))
frame=pd.DataFrame({'ds':dates,'y':y,'promotion':promotion})
model=Prophet(weekly_seasonality=True,yearly_seasonality=False,daily_seasonality=False,changepoint_prior_scale=.05)
model.add_regressor('promotion');model.fit(frame.iloc[:cut])
# Promotion is scheduled/known here; realized future y is never provided to predict.
predictions['Prophet']=model.predict(frame.iloc[cut:][['ds','promotion']])['yhat'].to_numpy()
results={}
for name,pred in predictions.items():
    assert pred.shape==(horizon,) and np.isfinite(pred).all(),name
    results[name]={'MAE':float(np.mean(np.abs(actual-pred))),'RMSE':float(np.sqrt(np.mean((actual-pred)**2)))}
print(json.dumps(results,indent=2))
# A caller can save stdout; importing this file is not intended as a library API.
