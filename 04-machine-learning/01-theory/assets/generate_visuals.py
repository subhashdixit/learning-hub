"""Reproducible teaching figures; run with numpy, scipy, sklearn, matplotlib, pillow."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
from matplotlib.patches import Circle, FancyArrowPatch
from scipy.cluster.hierarchy import linkage,dendrogram
from sklearn.datasets import make_moons,make_blobs,make_s_curve
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,QuadraticDiscriminantAnalysis
from sklearn.cluster import KMeans,DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest,GradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF,WhiteKernel
from sklearn.metrics import precision_recall_curve,roc_curve
OUT=Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True,parents=True)
rng=np.random.default_rng(42)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'white','axes.grid':True,'grid.alpha':.16})
blue='#2563eb';orange='#d97706';green='#059669';red='#dc2626'
files=[]
def save(name,fig):
 fig.tight_layout(pad=1.6);fig.savefig(OUT/name,dpi=145,bbox_inches='tight');plt.close(fig);files.append(name)
def panel(n=1,w=10,h=4):
 fig,ax=plt.subplots(1,n,figsize=(w,h),squeeze=False);return fig,ax[0]
# Scale geometry
fig,axs=panel(2);X=np.array([[20,20000],[30,22000],[40,80000]])
for ax,data,title in zip(axs,[X,StandardScaler().fit_transform(X)],['Raw: currency dominates distance','Standardized: both scales considered']):
 ax.scatter(data[:,0],data[:,1],s=90,c=[blue,orange,green]);
 for j,(a,b) in enumerate(data):ax.annotate('ABC'[j],(a,b),xytext=(7,7),textcoords='offset points')
 ax.set(title=title,xlabel='Age' if ax==axs[0] else 'Standardized age',ylabel='Income' if ax==axs[0] else 'Standardized income')
save('feature-scaling.png',fig)
# Polynomial fits
fig,axs=panel(3,w=13);x=np.linspace(-2,2,22);y=np.sin(2*x)+rng.normal(0,.22,len(x));xx=np.linspace(-2.1,2.1,400)
for ax,d,title in zip(axs,[1,4,18],['Underfit: degree 1','Useful flexibility: degree 4','Overfit: degree 18']):
 ax.scatter(x,y,c=blue,s=23);ax.plot(xx,np.polyval(np.polyfit(x,y,d),xx),c=orange);ax.set(xlabel='Input',ylabel='Target',ylim=(-2,2),title=title)
save('model-complexity.png',fig)
# Split patterns
fig,axs=panel(3,w=13)
n=20
for ax,title in zip(axs,['Independent-row folds','Grouped folds','Forward-time folds']):ax.set(title=title,xlabel='Observation order',ylabel='Evaluation round',yticks=range(4),ylim=(-.8,3.8))
for row in range(4):
 for col in range(n):
  val=(col%4==row);axs[0].scatter(col,row,c=orange if val else blue,marker='s',s=65)
  val=(col//5==row);axs[1].scatter(col,row,c=orange if val else blue,marker='s',s=65)
  end=8+row*3
  if col<end+3:axs[2].scatter(col,row,c=blue if col<end else orange,marker='s',s=65)
fig.suptitle('Blue = training; orange = validation; time folds leave future unused',y=1.03)
save('validation-schemes.png',fig)
# losses
fig,axs=panel();r=np.linspace(-3,3,400);ax=axs[0]
ax.plot(r,r*r/2,label='Half squared error',c=blue);ax.plot(r,np.abs(r),label='Absolute error',c=green);ax.plot(r,np.where(abs(r)<=1,r*r/2,abs(r)-.5),label='Huber (delta=1)',c=orange);ax.legend();ax.set(xlabel='Residual',ylabel='Loss',title='The chosen objective changes which mistakes matter most');save('loss-functions.png',fig)
# residuals
fig,axs=panel(3,w=13)
for ax,title in zip(axs,['No obvious remaining pattern','Missed curve','Changing error variance']):ax.axhline(0,c='gray',lw=1);ax.set(xlabel='Prediction',ylabel='Residual',title=title)
x=np.linspace(-2,2,160);axs[0].scatter(x,rng.normal(0,.4,len(x)),s=13,c=blue);axs[1].scatter(x,x*x-1.3+rng.normal(0,.25,len(x)),s=13,c=orange);axs[2].scatter(x,rng.normal(0,.2+.3*(x+2),len(x)),s=13,c=green);save('residual-diagnostics.png',fig)
# confusion plus threshold
fig,axs=panel(2,w=11);cm=np.array([[930,20],[10,40]]);axs[0].imshow(cm,cmap='Blues')
for i in range(2):
 for j in range(2):axs[0].text(j,i,str(cm[i,j]),ha='center',va='center',color='white' if cm[i,j]>400 else 'black',fontsize=17)
axs[0].set(xticks=[0,1],xticklabels=['Predicted -','Predicted +'],yticks=[0,1],yticklabels=['Actual -','Actual +'],title='Worked confusion matrix');axs[0].grid(False)
t=np.linspace(.02,.98,120);axs[1].plot(t,1-t**1.5,label='Recall (illustrative)',c=blue);axs[1].plot(t,.15+.8*t,label='Precision (illustrative)',c=orange);axs[1].set(xlabel='Decision threshold',ylabel='Metric',ylim=(0,1),title='Illustrative operating-point trade-off');axs[1].legend();save('classification-metrics.png',fig)
# penalty contours
fig,axs=panel(2)
g=np.linspace(-1.5,1.5,300);u,v=np.meshgrid(g,g)
for ax,pen,title in zip(axs,[u*u+v*v,abs(u)+abs(v)],['L2: smooth shrinkage','L1: corners permit zeros']):
 ax.contour(u,v,(u-.9)**2+2*(v-.35)**2,levels=[.1,.3,.7,1.2],colors=blue,alpha=.7);ax.contour(u,v,pen,levels=[.7],colors=orange,linewidths=3);ax.axhline(0,color='gray',lw=.8);ax.axvline(0,color='gray',lw=.8);ax.set(aspect='equal',xlabel='Coefficient 1',ylabel='Coefficient 2',title=title)
save('regularization-geometry.png',fig)
# logistic
fig,axs=panel(2);z=np.linspace(-6,6,300);p=1/(1+np.exp(-z));axs[0].plot(z,p,c=blue);axs[0].axhline(.5,c=orange,ls='--');axs[0].set(xlabel='Linear score / log odds',ylabel='Positive probability',title='Sigmoid maps scores to probabilities')
pp=np.linspace(.01,.99,300);axs[1].plot(pp,-np.log(pp),label='Actual y=1',c=blue);axs[1].plot(pp,-np.log(1-pp),label='Actual y=0',c=orange);axs[1].legend();axs[1].set(xlabel='Predicted positive probability',ylabel='Log loss',title='Confidently wrong predictions cost more');save('logistic-probability.png',fig)
# boundaries helper
X1=rng.multivariate_normal([-1,0],[[.4,.1],[.1,1]],140);X2=rng.multivariate_normal([1,0],[[1,-.5],[-.5,.6]],140);X=np.r_[X1,X2];y=np.r_[np.zeros(140),np.ones(140)]
u,v=np.meshgrid(np.linspace(-4,4,180),np.linspace(-3,3,180));grid=np.c_[u.ravel(),v.ravel()]
fig,axs=panel(2)
for ax,model,title in zip(axs,[LinearDiscriminantAnalysis(),QuadraticDiscriminantAnalysis()],['LDA: shared covariance','QDA: class-specific covariance']):
 model.fit(X,y);pred=model.predict(grid).reshape(u.shape);ax.contourf(u,v,pred,alpha=.12,cmap='coolwarm');ax.scatter(X[:,0],X[:,1],c=y,cmap='coolwarm',s=10);ax.set(title=title,xlabel='Feature 1',ylabel='Feature 2')
save('discriminant-boundaries.png',fig)
X,y=make_moons(n_samples=150,noise=.23,random_state=42);u,v=np.meshgrid(np.linspace(-1.6,2.6,180),np.linspace(-1,1.6,180));grid=np.c_[u.ravel(),v.ravel()]
fig,axs=panel(3,w=13)
for ax,k in zip(axs,[1,9,45]):
 model=KNeighborsClassifier(n_neighbors=k).fit(X,y);ax.contourf(u,v,model.predict(grid).reshape(u.shape),alpha=.15,cmap='coolwarm');ax.scatter(X[:,0],X[:,1],c=y,cmap='coolwarm',s=15);ax.set(title=f'KNN: k={k}',xlabel='Feature 1',ylabel='Feature 2')
save('knn-boundaries.png',fig)
# tree
fig,axs=panel(2,w=11);h=np.array([160,165,170,175,180]);target=np.array([50,65,85,70,90]);axs[0].scatter(h,target,c=blue,s=70);axs[0].axhline(72,c='gray',ls='--',label='Parent mean 72');axs[0].plot([159,162.5],[50,50],c=orange,lw=3);axs[0].plot([162.5,181],[77.5,77.5],c=orange,lw=3,label='Leaf predictions');axs[0].axvline(162.5,c=green,ls=':');axs[0].set(title='Regression tree: split at 162.5',xlabel='Height',ylabel='Target');axs[0].legend(fontsize=9)
p=np.linspace(.001,.999,300);axs[1].plot(p,1-p*p-(1-p)**2,label='Gini',c=blue);axs[1].plot(p,-p*np.log2(p)-(1-p)*np.log2(1-p),label='Entropy (bits)',c=orange);axs[1].legend();axs[1].set(title='Both peak when classes are mixed',xlabel='Positive class proportion',ylabel='Impurity');save('tree-splits.png',fig)
fig,axs=panel();b=np.arange(1,201)
for rho,c in zip([0,.2,.5,.9],[blue,green,orange,red]):axs[0].plot(b,rho+(1-rho)/b,label=f'Pairwise correlation {rho}',c=c)
axs[0].legend();axs[0].set(xlabel='Number of averaged models',ylabel='Variance (individual variance=1)',title='Averaging cannot eliminate shared errors');save('ensemble-variance.png',fig)
fig,axs=panel(2);axs[0].bar(range(1,8),np.ones(7)/7,color=blue);axs[1].bar(range(1,8),[1/12]*6+[.5],color=[blue]*6+[orange])
for ax,title in zip(axs,['Before first stump','After one mistake (example 7)']):ax.set(xlabel='Training example',ylabel='Normalized weight',ylim=(0,.55),title=title)
save('adaboost-weights.png',fig)
fig,axs=panel(3,w=13);x=np.linspace(-2,2,120).reshape(-1,1);y=np.sin(2*x[:,0])+rng.normal(0,.15,len(x))
for ax,n in zip(axs,[1,5,40]):
 model=GradientBoostingRegressor(n_estimators=n,max_depth=1,learning_rate=.2,random_state=42).fit(x,y);ax.scatter(x[:,0],y,s=10,alpha=.5,c=blue);ax.plot(x[:,0],model.predict(x),c=orange,lw=2);ax.set(title=f'{n} correction trees',xlabel='Input',ylabel='Target')
save('boosting-stages.png',fig)
# actual kmeans animation
X,_=make_blobs(n_samples=160,centers=[[-2,-1],[0,2],[2,-1]],cluster_std=.6,random_state=42);centres=np.array([[-3,2],[-1,0],[1,0]],float);states=[]
for t in range(7):
 lab=np.argmin(((X[:,None,:]-centres[None,:,:])**2).sum(2),axis=1);states.append((centres.copy(),lab.copy()));centres=np.array([X[lab==j].mean(0) if (lab==j).any() else centres[j] for j in range(3)])
fig,ax=plt.subplots(figsize=(7,4.6))
def frame(t):
 ax.clear();c,l=states[t];ax.scatter(X[:,0],X[:,1],c=l,cmap='viridis',s=22);ax.scatter(c[:,0],c[:,1],c='red',marker='X',s=170,edgecolors='white');ax.set(xlim=(-4,4),ylim=(-3,4),xlabel='Feature 1',ylabel='Feature 2',title=f'K-means assignment / update: round {t+1}')
ani=FuncAnimation(fig,frame,frames=len(states),interval=950);ani.save(OUT/'kmeans-iterations.gif',writer=PillowWriter(fps=1));plt.close(fig);files.append('kmeans-iterations.gif')
fig,axs=panel();dendrogram(linkage(np.array([[1],[2],[3],[8],[9],[10]]),method='complete'),labels=['1','2','3','8','9','10'],ax=axs[0]);axs[0].set(title='Complete linkage: join close groups, then distant groups',xlabel='Observation',ylabel='Merge dissimilarity');save('hierarchical-dendrogram.png',fig)
X,y=make_moons(n_samples=220,noise=.06,random_state=42);X=np.r_[X,[[2.5,1.5],[-1.5,-.6]]];fig,axs=panel(2)
for ax,model,title in zip(axs,[KMeans(2,n_init=10,random_state=42),DBSCAN(eps=.22,min_samples=5)],['K-means forces compact partitions','DBSCAN follows dense connected shapes']):
 lab=model.fit_predict(X);ax.scatter(X[:,0],X[:,1],c=lab,cmap='viridis',s=19);ax.set(title=title,xlabel='Feature 1',ylabel='Feature 2')
save('density-clustering.png',fig)
X=np.r_[rng.multivariate_normal([-1,0],[[1,.6],[.6,.6]],150),rng.multivariate_normal([2,1],[[.5,-.3],[-.3,1]],150)];mix=GaussianMixture(2,random_state=42).fit(X);u,v=np.meshgrid(np.linspace(-4,5,180),np.linspace(-3,4,180));grid=np.c_[u.ravel(),v.ravel()];fig,axs=panel();ax=axs[0];ax.scatter(X[:,0],X[:,1],c=mix.predict_proba(X)[:,0],cmap='coolwarm',s=16);ax.contour(u,v,np.exp(mix.score_samples(grid)).reshape(u.shape),levels=6,colors='gray',alpha=.6);ax.set(title='Gaussian mixture: colour shows soft responsibility',xlabel='Feature 1',ylabel='Feature 2');save('gaussian-mixture.png',fig)
# PCA exact example
X=np.array([[-2,-1],[-1,-2],[1,2],[2,1]]);proj=np.c_[X.mean(1),X.mean(1)];fig,axs=panel();ax=axs[0];ax.plot([-3,3],[-3,3],c=green,label='First principal direction');ax.scatter(X[:,0],X[:,1],c=blue,s=80,label='Original');ax.scatter(proj[:,0],proj[:,1],c=orange,s=80,label='Rank-1 reconstruction')
for a,b in zip(X,proj):ax.plot([a[0],b[0]],[a[1],b[1]],ls='--',c='gray')
ax.set(aspect='equal',xlabel='Feature 1',ylabel='Feature 2',title='PCA keeps 90% variance; reconstruction SSE = 2');ax.legend();save('pca-projection.png',fig)
X,t=make_s_curve(450,noise=.025,random_state=42);fig,axs=panel(2,w=11)
for ax,Z,title in zip(axs,[PCA(2).fit_transform(X),Isomap(n_neighbors=12,n_components=2).fit_transform(X)],['Linear PCA projection','Isomap uses graph-path geometry']):ax.scatter(Z[:,0],Z[:,1],c=t,cmap='viridis',s=10);ax.set(title=title,xlabel='Coordinate 1',ylabel='Coordinate 2')
save('manifold-projections.png',fig)
X=np.r_[rng.normal(0,.6,(200,2)),[[3,3],[-3,2],[2,-3]]];iso=IsolationForest(random_state=42,contamination=.03).fit(X);u,v=np.meshgrid(np.linspace(-4,4,150),np.linspace(-4,4,150));grid=np.c_[u.ravel(),v.ravel()];fig,axs=panel();ax=axs[0];z=iso.decision_function(grid).reshape(u.shape);im=ax.contourf(u,v,z,levels=20,cmap='Blues');ax.contour(u,v,z,levels=[0],colors=orange);ax.scatter(X[:,0],X[:,1],s=15,c='black');fig.colorbar(im,ax=ax,label='Decision score (larger = more normal)');ax.set(title='Isolation forest: threshold is a chosen operating rule',xlabel='Feature 1',ylabel='Feature 2');save('anomaly-detection.png',fig)
# prevalence precision
fig,axs=panel();fpr=np.linspace(.0001,.2,300);tpr=.8
for prevalence,c in zip([.01,.1,.5],[blue,orange,green]):
 precision=tpr*prevalence/(tpr*prevalence+fpr*(1-prevalence));axs[0].plot(fpr,precision,label=f'Positive prevalence {prevalence:.0%}',c=c)
axs[0].legend();axs[0].set(xlabel='False positive rate (recall fixed at 0.8)',ylabel='Precision',title='The same error rates yield different precision across populations');save('imbalance-pr-curve.png',fig)
# GP
x=np.array([-3,-1.8,-.5,.4,1.6])[:,None];y=np.sin(x[:,0])+rng.normal(0,.1,len(x));xx=np.linspace(-5,5,350)[:,None];gp=GaussianProcessRegressor(kernel=RBF(1)+WhiteKernel(.03),optimizer=None,alpha=1e-8).fit(x,y);mu,std=gp.predict(xx,return_std=True);fig,axs=panel();ax=axs[0];ax.plot(xx,mu,c=blue,label='Posterior predictive mean');ax.fill_between(xx[:,0],mu-1.96*std,mu+1.96*std,color=blue,alpha=.17,label='Approx. 95% observation interval');ax.scatter(x,y,c=orange,s=60,label='Observed');ax.set(title='GP predictions depend on kernel and noise assumptions',xlabel='Input',ylabel='Target');ax.legend(fontsize=9);save('gaussian-process.png',fig)
fig,axs=panel(3,w=12);P=np.array([[1,2],[2,.5],[.5,1.5],[1,1]]);Q=np.array([[2,0],[0,2],[1,1]]);rating=P@Q.T
for ax,mat,title in zip(axs,[P,Q.T,rating],['User factors (4 x 2)','Item factors (2 x 3)','Scores = product (4 x 3)']):
 ax.imshow(mat,cmap='Blues',vmin=0,vmax=4);ax.grid(False);ax.set(title=title,xticks=range(mat.shape[1]),yticks=range(mat.shape[0]));
 for i in range(mat.shape[0]):
  for j in range(mat.shape[1]):ax.text(j,i,f'{mat[i,j]:g}',ha='center',va='center',color='white' if mat[i,j]>2.5 else 'black')
save('recommendation-matrix.png',fig)
fig,axs=panel();ax=axs[0];ax.axis('off');ax.add_patch(Circle((.4,.5),.24,fc=blue,alpha=.25));ax.add_patch(Circle((.6,.5),.21,fc=orange,alpha=.3));ax.text(.27,.5,'Bread\n40 baskets',ha='center');ax.text(.73,.5,'Butter\n30 baskets',ha='center');ax.text(.5,.5,'Both\n20',ha='center',fontweight='bold');ax.text(.5,.12,'100 baskets: support = 0.20; confidence = 0.50; lift = 1.67',ha='center');ax.set(title='Co-occurrence is an association, not an intervention',xlim=(0,1),ylim=(0,1),aspect='equal');save('association-rules.png',fig)
fig,axs=panel(2);x=np.linspace(0,1,150);noise=rng.normal(0,.1,len(x));axs[0].scatter(x,x+noise,s=15,c=blue,label='Earlier: y increases with x');axs[0].scatter(x,1-x+noise,s=15,c=orange,label='Later: y decreases with x');axs[0].legend(fontsize=8);axs[0].set(title='Concept changes while inputs can stay stable',xlabel='Input x',ylabel='Outcome y');axs[1].hist(x,bins=10,color=blue,alpha=.4,label='Earlier input');axs[1].hist(x,bins=10,histtype='step',lw=2,color=orange,label='Later input');axs[1].legend();axs[1].set(title='Input distributions overlap completely',xlabel='Input x',ylabel='Count');save('concept-drift.png',fig)
fig,axs=panel();ax=axs[0];ax.axis('off');ax.text(.2,.6,'AGENT\npolicy / value',ha='center',va='center',bbox=dict(boxstyle='round,pad=1',fc='#dbeafe'));ax.text(.8,.6,'ENVIRONMENT\nstate transitions',ha='center',va='center',bbox=dict(boxstyle='round,pad=1',fc='#fef3c7'));ax.annotate('',xy=(.66,.77),xytext=(.34,.77),arrowprops=dict(arrowstyle='->',lw=2,color=blue));ax.text(.5,.85,'action',ha='center');ax.annotate('',xy=(.34,.38),xytext=(.66,.38),arrowprops=dict(arrowstyle='->',lw=2,color=orange));ax.text(.5,.25,'reward + next observation',ha='center');ax.set(title='Action choices influence future experience',xlim=(0,1),ylim=(0,1));save('rl-loop.png',fig)
fig,axs=panel();ax=axs[0];ax.axis('off');layers=[[.25,.5,.75],[.2,.4,.6,.8],[.35,.65],[.5]]
for l in range(len(layers)-1):
 for a in layers[l]:
  for b in layers[l+1]:ax.plot([l,l+1],[a,b],c='gray',alpha=.3,zorder=1)
for l,ys in enumerate(layers):ax.scatter([l]*len(ys),ys,s=400,c=[blue,green,orange,red][l],zorder=2)
for l,label in enumerate(['Input','Hidden layer','Representation','Output']):ax.text(l,.02,label,ha='center')
ax.annotate('Forward: prediction',xy=(2.8,.98),xytext=(.1,.98),arrowprops=dict(arrowstyle='->',color=blue));ax.annotate('Backward: loss gradients',xy=(.1,-.12),xytext=(2.8,-.12),arrowprops=dict(arrowstyle='->',color=red),ha='right');ax.set(title='Nonlinear layers learn representations; gradients train them',xlim=(-.3,3.3),ylim=(-.25,1.15));save('neural-network.png',fig)
fig,axs=panel();ax=axs[0]
for i,end in enumerate([12,18,24,30]):ax.barh(i,end,color=blue);ax.barh(i,6,left=end,color=orange)
ax.set(xlabel='Month',ylabel='Backtest origin',yticks=range(4),yticklabels=['1','2','3','4'],title='Train on the past (blue), predict next horizon (orange)');save('time-backtest.png',fig)
fig,axs=panel(2);x=np.linspace(0,1,150)
for i in range(6):axs[0].plot(x,(.3+i*.13)*x + (i-2.5)*.08,alpha=.7)
axs[0].plot(x,.625*x,c='black',lw=3,label='Illustrative mean curve');axs[0].legend(fontsize=8);axs[0].set(title='ICE curves can differ behind an average',xlabel='Varied feature',ylabel='Prediction')
vals=[30,15,-5];axs[1].barh(['Feature A','Feature B','Feature C'],vals,color=[blue,blue,orange]);axs[1].axvline(0,c='gray');axs[1].set(title='Additive explanation: 60 + 30 + 15 - 5 = 100',xlabel='Contribution on chosen output scale');save('interpretability.png',fig)
fig,axs=panel();ax=axs[0];x=np.linspace(0,10,60);mean=2*x;actual=mean+rng.normal(0,2.4,len(x));ax.fill_between(x,mean-5,mean+5,color=blue,alpha=.18,label='Illustrative calibrated interval');ax.plot(x,mean,c=blue,label='Point prediction');inside=abs(actual-mean)<=5;ax.scatter(x[inside],actual[inside],c=green,s=19,label='Covered');ax.scatter(x[~inside],actual[~inside],c=red,s=28,label='Not covered');ax.legend();ax.set(title='Assess coverage, width and coverage by subgroup',xlabel='Input',ylabel='Outcome');save('conformal-intervals.png',fig)
print('Generated',len(files),'figures:',files)
