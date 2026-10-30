"""Regression calculations and gradient descent. Synthetic teaching example; no remote data required."""
import numpy as np
x=np.array([1.,2.,3.]); y=x.copy(); b=w=0.
gb=np.mean(b+w*x-y);gw=np.mean((b+w*x-y)*x)
assert np.isclose(gb,-2) and np.isclose(gw,-14/3)
b,w=b-.1*gb,w-.1*gw
assert np.allclose([b,w],[.2,7/15])
for _ in range(3000):
 r=b+w*x-y;b,w=b-.05*r.mean(),w-.05*np.mean(r*x)
assert np.mean((b+w*x-y)**2)<1e-7
X=np.c_[np.ones(len(x)),x];coef=np.linalg.lstsq(X,y,rcond=None)[0]
assert np.allclose(coef,[0,1]);print('Gradient fit:',b,w,'; least-squares:',coef)
