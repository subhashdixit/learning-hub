"""Calibrate prediction intervals and evaluate finite-sample coverage. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
rng=np.random.default_rng(42);X=rng.uniform(-3,3,(1200,1));y=2*X[:,0]+rng.normal(0,1.2,len(X))
Xdev,Xtest,ydev,ytest=train_test_split(X,y,test_size=400,random_state=42)
Xtr,Xcal,ytr,ycal=train_test_split(Xdev,ydev,test_size=300,random_state=43)
model=LinearRegression().fit(Xtr,ytr);scores=np.abs(ycal-model.predict(Xcal));alpha=.1
k=int(np.ceil((len(scores)+1)*(1-alpha)));q=np.inf if k>len(scores) else np.sort(scores)[k-1]
pred=model.predict(Xtest);coverage=np.mean(np.abs(ytest-pred)<=q)
assert np.isfinite(q) and q>0 and 0<=coverage<=1
example=np.array([1,1,2,2,3,3,4,5,8]);assert example[int(np.ceil(10*.8))-1]==5
print('Calibration radius:',round(q,3),'test coverage:',round(coverage,3),'width:',round(2*q,3))
# Coverage varies on a finite test; there is no assertion that one test fraction equals exactly 90%.
