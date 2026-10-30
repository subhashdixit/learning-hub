"""Compare regression pipelines with an untouched test. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split,GridSearchCV,KFold
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error
X,y=make_regression(n_samples=500,n_features=12,n_informative=7,noise=12,random_state=42)
X[::17,0]=np.nan
Xt,Xs,yt,ys=train_test_split(X,y,test_size=.25,random_state=42)
pipe=make_pipeline(SimpleImputer(),StandardScaler(),Ridge())
search=GridSearchCV(pipe,{'ridge__alpha':[.01,.1,1,10,100]},cv=KFold(5,shuffle=True,random_state=42),scoring='neg_mean_squared_error').fit(Xt,yt)
pred=search.predict(Xs);baseline=DummyRegressor().fit(Xt,yt).predict(Xs)
rmse=np.sqrt(mean_squared_error(ys,pred));base=np.sqrt(mean_squared_error(ys,baseline))
assert rmse<base;print('Chosen:',search.best_params_,'test RMSE:',round(rmse,3),'baseline:',round(base,3))
