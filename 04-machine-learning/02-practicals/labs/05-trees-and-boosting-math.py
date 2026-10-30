"""Reproduce tree, AdaBoost and second-order leaf arithmetic. Synthetic teaching example; no remote data required."""
import numpy as np
x=np.array([160,165,170,175,180]);y=np.array([50,65,85,70,90.])
parent=np.mean((y-y.mean())**2);left=x<=162.5
pred=np.where(left,y[left].mean(),y[~left].mean());child=np.mean((y-pred)**2)
assert np.isclose(parent,206) and np.isclose(child,85)
eps=1/7;alpha=.5*np.log((1-eps)/eps);margin=np.array([1.]*6+[-1.])
w=np.exp(-alpha*margin)/7;w/=w.sum();assert np.allclose(w,[1/12]*6+[.5])
leaf_score=-(-6)/(2+1);assert leaf_score==2
print('Tree gain:',parent-child,'AdaBoost weights:',w,'regularized leaf:',leaf_score)
