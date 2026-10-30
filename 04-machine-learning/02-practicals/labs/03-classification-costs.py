"""Select a classification threshold without test leakage. Synthetic teaching example; no remote data required."""
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,average_precision_score,brier_score_loss
X,y=make_classification(n_samples=2400,n_features=12,n_informative=6,weights=[.94,.06],class_sep=1.5,random_state=42)
Xd,Xtest,yd,ytest=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
Xtr,Xval,ytr,yval=train_test_split(Xd,yd,test_size=1/3,stratify=yd,random_state=43)
model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000)).fit(Xtr,ytr)
p=model.predict_proba(Xval)[:,1]
def cost(y,p,t):
 tn,fp,fn,tp=confusion_matrix(y,p>=t,labels=[0,1]).ravel();return fp+20*fn
thresholds=np.linspace(.01,.99,99);chosen=thresholds[np.argmin([cost(yval,p,t) for t in thresholds])]
pt=model.predict_proba(Xtest)[:,1];cm=confusion_matrix(ytest,pt>=chosen,labels=[0,1])
assert cm.sum()==len(ytest) and 0<chosen<1
print('Validation-chosen threshold:',chosen,'; test confusion matrix:\n',cm)
print('Test average precision:',round(average_precision_score(ytest,pt),3),'Brier:',round(brier_score_loss(ytest,pt),3))
# A synthetic result is not a promise of real-world fraud performance.
