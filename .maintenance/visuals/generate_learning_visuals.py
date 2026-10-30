"""Generate synthetic teaching plots; requires NumPy, Matplotlib and Pillow."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
from matplotlib.patches import Rectangle
ROOT=Path('work/learning-hub')
if not ROOT.exists():ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(42);blue='#2563eb';orange='#d97706';green='#059669';red='#dc2626'
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.16,'figure.facecolor':'white'})
outputs=[]
def out(prefix,name):
 p=next(ROOT.glob(prefix+'-*'))/'01-theory/assets';p.mkdir(exist_ok=True,parents=True);return p/name
def save(prefix,name,fig):
 fig.tight_layout(pad=1.5);fig.savefig(out(prefix,name),dpi=145,bbox_inches='tight');plt.close(fig);outputs.append((prefix,name))
def panel(n=1,w=10,h=4):
 f,a=plt.subplots(1,n,figsize=(w,h),squeeze=False);return f,a[0]
f,axs=plt.subplots(1,2,figsize=(12,4.5))
def box(ax,x,y,label,color):ax.text(x,y,label,ha='center',va='center',fontsize=10,bbox=dict(boxstyle='round,pad=.5',fc=color,ec='gray'))
def arrow(ax,a,b):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.8))
a=axs[0];a.set_title('Assignment: both names point to the same outer list');box(a,.12,.75,'name A','#dbeafe');box(a,.12,.25,'name B','#dbeafe');box(a,.52,.5,'outer list','#fef3c7');box(a,.87,.5,'inner list','#dcfce7');arrow(a,(.22,.72),(.42,.54));arrow(a,(.22,.28),(.42,.46));arrow(a,(.62,.5),(.77,.5))
a=axs[1];a.set_title('Shallow copy: separate outer lists share nested data');box(a,.1,.75,'name A','#dbeafe');box(a,.1,.25,'name B','#dbeafe');box(a,.48,.75,'original outer','#fef3c7');box(a,.48,.25,'copied outer','#fef3c7');box(a,.87,.5,'inner list','#dcfce7');arrow(a,(.2,.75),(.35,.75));arrow(a,(.2,.25),(.35,.25));arrow(a,(.62,.73),(.78,.54));arrow(a,(.62,.27),(.78,.46))
for a in axs:a.set(xlim=(0,1),ylim=(0,1));a.axis('off')
save('01','references.png',f)
f,axs=panel();n=np.arange(1,101);axs[0].plot(n,n,label='Retained full result (illustrative units)',c=blue);axs[0].plot(n,np.ones_like(n)*3,label='Bounded pipeline working set (illustrative)',c=orange);axs[0].legend();axs[0].set(title='Laziness can avoid storing every result; input/consumer still matter',xlabel='Items processed',ylabel='Illustrative retained items');save('01','lazy-stream.png',f)
f,axs=panel();x=np.linspace(-1,5,250);axs[0].plot(x,(x-3)**2,c=blue);w=0;ws=[w]
for _ in range(9):w-=.1*2*(w-3);ws.append(w)
axs[0].plot(ws,[(w-3)**2 for w in ws],'o-',c=orange,label='Gradient updates, rate 0.1');axs[0].set(title='Minimize J(w) = (w - 3)²',xlabel='Parameter w',ylabel='Loss');axs[0].legend();save('02','gradient.png',f)
f,axs=panel(2);sets=[[2,4,6],[2,4,6,100]]
for ax,data in zip(axs,sets):
 ax.scatter(data,np.zeros(len(data)),s=80,c=blue);ax.axvline(np.mean(data),c=orange,label=f'Mean {np.mean(data):g}');ax.axvline(np.median(data),c=green,ls='--',label=f'Median {np.median(data):g}');ax.set(xlabel='Observed value',yticks=[],title='Before outlier' if len(data)==3 else 'After adding 100');ax.legend()
save('02','mean-median.png',f)
f,axs=panel(3,w=13)
for ax,n in zip(axs,[1,5,30]):
 values=rng.exponential(1,(6000,n)).mean(1);ax.hist(values,bins=45,color=blue,alpha=.8,density=True);ax.axvline(1,c=orange);ax.set(title=f'Mean of {n} independent draws',xlabel='Sample mean',ylabel='Density',xlim=(0,4))
f.suptitle('Exponential observations: averages concentrate around population mean 1',y=1.03);save('02','clt.png',f)
f,axs=panel();ax=axs[0];samples=rng.normal(0,1,(35,40));means=samples.mean(1);half=1.96/np.sqrt(40)
for i,m in enumerate(means):ax.plot([m-half,m+half],[i,i],c=blue if abs(m)<=half else red);ax.scatter(m,i,s=10,c='black')
ax.axvline(0,c=green,ls='--',label='Fixed population mean');ax.set(title='35 normal-sample intervals using known SD; some miss',xlabel='Mean estimate and nominal 95% interval',ylabel='Repeated sample');ax.legend();save('02','confidence-coverage.png',f)
f,axs=panel(2);axs[0].bar(['Left matches','Right matches','Joined rows'],[2,3,6],color=[blue,green,orange]);axs[0].set(title='One key: 2 x 3 = 6 combinations',ylabel='Rows');axs[1].imshow(np.ones((2,3)),cmap='Blues',vmin=0,vmax=1);axs[1].set(xticks=range(3),xticklabels=['R1','R2','R3'],yticks=range(2),yticklabels=['L1','L2'],title='Every matching pair appears');axs[1].grid(False)
for i in range(2):
 for j in range(3):axs[1].text(j,i,f'L{i+1}, R{j+1}',ha='center',va='center',color='white')
save('03','join-multiplicity.png',f)
f,axs=panel();labels=['100 first','100 second','80'];x=np.arange(3);width=.24
for shift,vals,label,col in zip([-width,0,width],[[1,2,3],[1,1,3],[1,1,2]],['ROW_NUMBER (chosen tie order)','RANK','DENSE_RANK'],[blue,orange,green]):axs[0].bar(x+shift,vals,width,label=label,color=col)
axs[0].set(xticks=x,xticklabels=labels,title='Equal values share rank, but row numbers remain distinct',ylabel='Assigned number');axs[0].legend(fontsize=8);save('03','ranking.png',f)
f,axs=panel(2);x=np.linspace(-5,5,300);sig=1/(1+np.exp(-x));axs[0].plot(x,np.maximum(0,x),label='ReLU',c=blue);axs[0].plot(x,np.tanh(x),label='tanh',c=orange);axs[0].plot(x,sig,label='sigmoid',c=green);axs[1].plot(x,(x>0).astype(float),label='ReLU (except at zero)',c=blue);axs[1].plot(x,1-np.tanh(x)**2,label='tanh',c=orange);axs[1].plot(x,sig*(1-sig),label='sigmoid',c=green)
for ax,title in zip(axs,['Activation outputs','Derivative magnitudes']):ax.set(xlabel='Input',ylabel='Value',title=title);ax.legend(fontsize=8)
save('05','activations.png',f)
f,axs=panel(3,w=12);mat=np.arange(1,10).reshape(3,3);kernel=np.array([[1,0],[0,-1]]);result=np.array([[np.sum(mat[i:i+2,j:j+2]*kernel) for j in range(2)] for i in range(2)])
for ax,arr,title in zip(axs,[mat,kernel,result],['Input','Shared 2 x 2 kernel','Valid cross-correlation output']):
 ax.imshow(arr,cmap='Blues');ax.grid(False);ax.set(title=title,xticks=[],yticks=[])
 for i in range(arr.shape[0]):
  for j in range(arr.shape[1]):ax.text(j,i,str(arr[i,j]),ha='center',va='center',color='black',bbox=dict(fc='white',alpha=.7,ec='none'))
save('05','convolution.png',f)
f,axs=panel(2);scores=np.array([[1,0,-1],[0,1,.5],[.2,.8,1.2]])
for ax,causal,title in zip(axs,[False,True],['Unmasked self-attention','Causal attention: no future keys']):
 z=scores.copy()
 if causal:z[np.triu_indices(3,1)]=-np.inf
 w=np.exp(z-np.max(z,axis=1,keepdims=True));w/=w.sum(1,keepdims=True);ax.imshow(w,vmin=0,vmax=1,cmap='Blues');ax.grid(False);ax.set(title=title,xlabel='Key position',ylabel='Query position',xticks=range(3),yticks=range(3))
 for i in range(3):
  for j in range(3):ax.text(j,i,f'{w[i,j]:.2f}',ha='center',va='center',color='black' if w[i,j]<.6 else 'white')
save('05','attention.png',f)
t=np.arange(84);trend=20+.05*t;season=3*np.sin(2*np.pi*t/7);noise=rng.normal(0,.4,len(t));f,ax=plt.subplots(4,1,figsize=(10,8),sharex=True)
for a,v,title in zip(ax,[trend+season+noise,trend,season,noise],['Observed = trend + seasonality + remainder','Trend','Weekly seasonality','Remainder']):a.plot(t,v,c=blue);a.set(ylabel=title.split()[0],title=title)
ax[-1].set_xlabel('Day');save('06','decomposition.png',f)
f,axs=panel();y=trend+season+noise;ax=axs[0];ax.plot(t,y,c='gray',alpha=.65,label='Actual series')
for origin,col in zip([42,56,70],[blue,orange,green]):ax.plot(np.arange(origin,origin+7),y[origin-7:origin],'o--',c=col,label=f'Seasonal-naive forecast at day {origin}')
ax.set(title='Issued seven-day forecasts use the previous available week',xlabel='Day',ylabel='Target');ax.legend(fontsize=8);save('06','forecast-origins.png',f)
f,axs=panel();ax=axs[0]
for v,label,col in [([1,0],'query',blue),([2,0],'A: cosine 1',green),([0,3],'B: cosine 0',orange),([1,1],'C: cosine 0.707',red)]:ax.arrow(0,0,*v,width=.015,length_includes_head=True,color=col,alpha=.75);ax.text(v[0]+.08,v[1]+.08,label,color=col)
ax.set(xlim=(-.2,3.5),ylim=(-.2,3.5),aspect='equal',xlabel='Embedding coordinate 1',ylabel='Embedding coordinate 2',title='Illustrative vectors: direction and length are different');save('07','vector-search.png',f)
f,axs=panel();ax=axs[0];ax.bar(['Correct evidence\ncorrect answer','Missing evidence','Evidence present\nmisused','Unsupported\ncitation'],[60,20,15,5],color=[green,orange,blue,red]);ax.set(title='Hypothetical 100-case RAG audit: fix the actual failure stage',ylabel='Illustrative case count');save('07','rag-diagnostics.png',f)
f,axs=panel();ax=axs[0];stages=['Retrieve','Rerank','Generate','Validate'];values=[80,120,700,40];left=0
for label,val,col in zip(stages,values,[blue,orange,green,red]):ax.barh(['One request'],[val],left=left,label=label,color=col);ax.text(left+val/2,0,str(val),ha='center',va='center',color='white',fontsize=9);left+=val
ax.set(title='Illustrative latency budget: every stage contributes',xlabel='Milliseconds');ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=4);save('07','latency-budget.png',f)
f,axs=panel();axs[0].bar(['Naive sum\n20 + 30 + replay 20','Unique events\na=20,b=30'],[70,50],color=[orange,blue]);axs[0].set(title='Deduplication depends on stable identity and update semantics',ylabel='Amount');save('08','deduplication.png',f)
f,axs=panel(2)
for ax,vals,title in zip(axs,[[25,25,25,25],[85,5,5,5]],['Balanced partitions','Skewed partitions']):ax.bar(range(1,5),vals,color=blue);ax.set(title=title,xlabel='Partition',ylabel='Illustrative work units',ylim=(0,90))
save('08','partition-skew.png',f)
f,axs=panel();axs[0].step(range(5),[0,5,25,50,100],where='post',c=blue,lw=2);axs[0].scatter(range(5),[0,5,25,50,100],c=green,s=55);axs[0].set(xticks=range(5),xticklabels=['Checks','Canary','Gate 1','Gate 2','Rollout'],ylabel='Illustrative traffic exposure (%)',title='Release exposure advances only when defined gates pass');save('09','release-gates.png',f)
f,axs=panel();lat=np.r_[rng.normal(20,3,950),rng.normal(250,20,50)];axs[0].hist(lat,bins=50,color=blue);axs[0].axvline(lat.mean(),c=orange,label=f'Mean {lat.mean():.0f} ms');axs[0].axvline(np.quantile(lat,.99),c=red,label=f'p99 {np.quantile(lat,.99):.0f} ms');axs[0].set(title='Synthetic latency distribution with a slow tail',xlabel='Milliseconds',ylabel='Requests');axs[0].legend();save('09','latency-tail.png',f)
f,axs=panel();years=np.arange(1,11)
for rate,col in zip([.02,.05,.15],[blue,green,orange]):axs[0].plot(years,110/(1+rate)**years,'o-',label=f'Illustrative discount rate {rate:.0%}',c=col)
axs[0].set(title='Present value of one 110-unit future cash flow',xlabel='Years until cash flow',ylabel='Present value');axs[0].legend();save('10','discounting.png',f)
f,axs=panel(2);wealth=np.array([100,120,90,110,130,100,125]);peak=np.maximum.accumulate(wealth);draw=wealth/peak-1;axs[0].plot(wealth,'o-',c=blue,label='Wealth');axs[0].plot(peak,'--',c=green,label='Running peak');axs[0].set(title='Synthetic wealth path',xlabel='Period',ylabel='Wealth');axs[0].legend();axs[1].fill_between(range(len(draw)),draw*100,0,color=orange,alpha=.4);axs[1].set(title='Drawdown from previous peak',xlabel='Period',ylabel='Drawdown (%)');save('10','wealth-drawdown.png',f)
f,axs=panel();n=np.arange(2,101)
for vals,label,col in [(np.log2(n),'log n',green),(n,'n',blue),(n*np.log2(n),'n log n',orange),(n*n,'n²',red)]:axs[0].plot(n,vals,label=label,c=col)
axs[0].set(yscale='log',xlabel='Input size n',ylabel='Illustrative operation growth (log scale)',title='Growth curves, not benchmark timings');axs[0].legend();save('11','complexity.png',f)
f,axs=panel();sessions=np.arange(1,9);identified=np.array([5,8,11,13,15,17,18,20]);resolved=np.array([1,3,5,8,10,13,15,18]);axs[0].plot(sessions,identified,'o-',label='Unique misconceptions recorded',c=orange);axs[0].plot(sessions,resolved,'o-',label='Successfully retried on changed cases',c=blue);axs[0].set(title='Illustrative practice log: assess transfer, not memorized answers',xlabel='Practice session',ylabel='Count');axs[0].legend();save('11','practice.png',f)
f,axs=panel(2);axs[0].bar(['Small row','Large row'],[50,10],color=[orange,blue]);axs[0].set(title='Row margins: revenue 100 vs 900',ylabel='Margin (%)');axs[1].bar(['Unweighted\nrow average','Total profit /\ntotal revenue'],[30,14],color=[orange,blue]);axs[1].set(title='Different denominators, different answers',ylabel='Margin (%)');save('12','weighted-margin.png',f)
f,axs=panel();data=np.array([[100,40,30,25],[100,45,35,np.nan],[100,42,np.nan,np.nan]]);im=axs[0].imshow(np.ma.masked_invalid(data),cmap='Blues',vmin=0,vmax=100);axs[0].grid(False);axs[0].set(xticks=range(4),xticklabels=['Start','Month 1','Month 2','Month 3'],yticks=range(3),yticklabels=['Jan','Feb','Mar'],title='Illustrative cohorts: unobserved future cells are blank')
for i in range(3):
 for j in range(4):
  if np.isfinite(data[i,j]):axs[0].text(j,i,f'{data[i,j]:.0f}%',ha='center',va='center',color='white' if data[i,j]>60 else 'black')
save('12','cohorts.png',f)
# Three real animated sequences, linked to their lessons.
f,ax=plt.subplots(figsize=(8,4.5));ws=[0.]
for _ in range(17):ws.append(ws[-1]-.1*2*(ws[-1]-3))
def gradframe(i):
 ax.clear();x=np.linspace(-1,5,200);ax.plot(x,(x-3)**2,c=blue);ax.plot(ws[:i+1],[(w-3)**2 for w in ws[:i+1]],'o-',c=orange);ax.set(xlim=(-1,5),ylim=(-.2,17),title=f'Gradient descent: update {i}, w={ws[i]:.3f}',xlabel='w',ylabel='J(w)')
FuncAnimation(f,gradframe,frames=len(ws)).save(out('02','gradient-descent.gif'),writer=PillowWriter(fps=3));plt.close(f);outputs.append(('02','gradient-descent.gif'))
f,ax=plt.subplots(figsize=(8,4.5));seq=[2,3,4,1,5,2,3]
def streamframe(i):
 ax.clear();ax.bar(range(i+1),seq[:i+1],color=blue);ax.set(xlim=(-.5,6.5),ylim=(0,6),title=f'Generator emits item {i+1}; running total = {sum(seq[:i+1])}',xlabel='Item position',ylabel='Value');ax.text(.04,.85,'One yield resumes the suspended loop',transform=ax.transAxes)
FuncAnimation(f,streamframe,frames=len(seq)).save(out('01','generator-stream.gif'),writer=PillowWriter(fps=1));plt.close(f);outputs.append(('01','generator-stream.gif'))
f,ax=plt.subplots(figsize=(9,4.5));t=np.arange(70);actual=20+.05*t+3*np.sin(2*np.pi*t/7)
def forecastframe(i):
 origin=28+7*i;ax.clear();ax.plot(t[:origin],actual[:origin],c=blue,label='Known history');ax.plot(t[origin:origin+7],actual[origin-7:origin],'o--',c=orange,label='Issued seasonal-naive forecast');ax.axvline(origin-.5,c='gray',ls=':');ax.set(xlim=(0,70),ylim=(16,28),title=f'Forecast origin day {origin}: future actuals are hidden',xlabel='Day',ylabel='Target');ax.legend(loc='upper left')
FuncAnimation(f,forecastframe,frames=6).save(out('06','rolling-forecast.gif'),writer=PillowWriter(fps=1));plt.close(f);outputs.append(('06','rolling-forecast.gif'))
print('Generated',len(outputs),'plots/animations')
