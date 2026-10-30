"""Compare clustering geometry and verify PCA reconstruction. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans,DBSCAN
from sklearn.metrics import adjusted_rand_score
from sklearn.decomposition import PCA
X,y=make_moons(n_samples=300,noise=.05,random_state=42)
for name,labels in [('kmeans',KMeans(2,n_init=10,random_state=42).fit_predict(X)),('dbscan',DBSCAN(eps=.2,min_samples=5).fit_predict(X))]:
 print(name,'external ARI:',round(adjusted_rand_score(y,labels),3),'noise:',int((labels==-1).sum()))
# Ground-truth labels are evaluation only; neither clustering fit receives y.
Z=np.array([[-2.,-1.],[-1.,-2.],[1.,2.],[2.,1.]])
pca=PCA(n_components=1).fit(Z);back=pca.inverse_transform(pca.transform(Z));sse=np.sum((Z-back)**2)
assert np.isclose(pca.explained_variance_ratio_[0],.9) and np.isclose(sse,2)
print('PCA retained fraction:',pca.explained_variance_ratio_[0],'reconstruction SSE:',sse)
