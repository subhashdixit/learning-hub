from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve,precision_recall_curve,roc_auc_score,average_precision_score
from sklearn.calibration import calibration_curve
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.15})
X,y=make_classification(n_samples=2400,n_features=12,n_informative=6,weights=[.94,.06],class_sep=1.5,random_state=42)
Xt,Xs,yt,ys=train_test_split(X,y,test_size=.3,stratify=y,random_state=42)
p=make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000)).fit(Xt,yt).predict_proba(Xs)[:,1]
fig,axs=plt.subplots(1,3,figsize=(14,4));fpr,tpr,_=roc_curve(ys,p);precision,recall,_=precision_recall_curve(ys,p);frac,mean=calibration_curve(ys,p,n_bins=7,strategy='quantile')
axs[0].plot(fpr,tpr,c='#2563eb');axs[0].plot([0,1],[0,1],'--',c='gray');axs[0].set(title=f'ROC: AUC = {roc_auc_score(ys,p):.3f}',xlabel='False positive rate',ylabel='True positive rate')
axs[1].plot(recall,precision,c='#d97706');axs[1].axhline(ys.mean(),c='gray',ls='--',label='Positive prevalence');axs[1].legend(fontsize=8);axs[1].set(title=f'Precision–recall: AP = {average_precision_score(ys,p):.3f}',xlabel='Recall',ylabel='Precision')
axs[2].plot(mean,frac,'o-',c='#059669');axs[2].plot([0,1],[0,1],'--',c='gray');axs[2].set(title='Reliability: seven quantile bins',xlabel='Mean predicted probability',ylabel='Observed positive fraction')
fig.suptitle('One held-out synthetic dataset: ranking and probability quality are distinct',y=1.05);fig.tight_layout();fig.savefig(OUT/'roc-pr-calibration.png',dpi=145,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,4));a,b=np.meshgrid(np.linspace(-3,3,150),np.linspace(-3,3,150));loss=a*a+5*b*b
for ax,eta in zip(axs,[.08,.23]):
 ax.contour(a,b,loss,levels=[.2,1,3,8,15,30,50],cmap='Blues');point=np.array([2.7,2.7]);points=[point.copy()]
 for _ in range(12):point=point-eta*np.array([2*point[0],10*point[1]]);points.append(point.copy())
 path=np.array(points);ax.plot(path[:,0],path[:,1],'o-',c='#d97706',markersize=3);ax.set(xlim=(-3,3),ylim=(-3,3),xlabel='Parameter 1',ylabel='Parameter 2',title=f'Learning rate {eta}: '+('converges' if eta<.2 else 'diverges; exits view'))
fig.suptitle('Quadratic objective: steps must respect curvature');fig.tight_layout();fig.savefig(OUT/'gradient-trajectories.png',dpi=145,bbox_inches='tight');plt.close(fig)
