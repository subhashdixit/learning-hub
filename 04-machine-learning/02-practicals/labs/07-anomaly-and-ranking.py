"""Inspect anomaly ranking and calculate NDCG. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.ensemble import IsolationForest
rng=np.random.default_rng(42);normal=rng.normal(0,.4,(300,2));X=np.r_[normal,[[4,4],[-4,4],[4,-4]]]
model=IsolationForest(random_state=42,contamination=.02).fit(X)
# score_samples is larger for more normal observations: reverse the order for alerts.
rank=np.argsort(model.score_samples(X));print('Top anomaly indices:',rank[:6])
assert set(range(300,303)).issubset(set(rank[:6]))
def dcg(relevance):return np.sum((2**np.array(relevance)-1)/np.log2(np.arange(len(relevance))+2))
ndcg=dcg([1,0,1])/dcg([1,1,0]);assert np.isclose(ndcg,.9197207891481876)
print('NDCG@3:',ndcg)
