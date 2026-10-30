"""Compare distinct supervised families on identical CV folds. Synthetic teaching example; no remote data required."""
from sklearn.datasets import make_moons
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier,HistGradientBoostingClassifier
X,y=make_moons(n_samples=500,noise=.25,random_state=42)
cv=StratifiedKFold(5,shuffle=True,random_state=42)
models={'logistic':make_pipeline(StandardScaler(),LogisticRegression()),'knn':make_pipeline(StandardScaler(),KNeighborsClassifier(15)),'svm':make_pipeline(StandardScaler(),SVC(C=2,gamma='scale')),'forest':RandomForestClassifier(n_estimators=100,min_samples_leaf=4,random_state=42),'boosting':HistGradientBoostingClassifier(max_iter=80,max_leaf_nodes=7,random_state=42)}
for name,model in models.items():
 scores=cross_val_score(model,X,y,cv=cv,scoring='balanced_accuracy')
 assert len(scores)==5;print(name,round(scores.mean(),3),'+/- fold SD',round(scores.std(),3))
# This is a development comparison; reporting a selected winner needs a separate evaluation.
