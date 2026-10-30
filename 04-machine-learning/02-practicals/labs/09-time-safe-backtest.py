"""Make lag features and compare a forecast with a naive baseline. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
rng=np.random.default_rng(42);n=260;t=np.arange(n);sales=20+.03*t+4*np.sin(2*np.pi*t/7)+rng.normal(0,.6,n)
# For predicting day t, every sales feature comes strictly before t.
days=np.arange(14,n);X=np.array([[sales[i-1],sales[i-7],sales[i-14],i] for i in days]);y=sales[days]
for fold,(tr,va) in enumerate(TimeSeriesSplit(n_splits=4,test_size=28).split(X),1):
 assert days[tr].max()<days[va].min()
 # One-step-ahead rolling-origin evaluation: yesterday's actual is available at each prediction.
 model=Ridge(alpha=1).fit(X[tr],y[tr]);p=model.predict(X[va]);naive=X[va,1]
 print('Fold',fold,'model MAE',round(mean_absolute_error(y[va],p),3),'seasonal-naive',round(mean_absolute_error(y[va],naive),3))
# This does not simulate predicting the entire next 28 days at one fixed origin.
