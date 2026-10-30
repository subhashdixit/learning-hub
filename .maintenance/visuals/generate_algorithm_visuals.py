"""Synthetic illustrations for algorithm motivations; none claims a fitted Prophet result."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path('work/learning-hub')
if not ROOT.exists():ROOT=Path(__file__).resolve().parents[2]
blue='#2563eb';orange='#d97706';green='#059669';red='#dc2626'
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.15})
def save(prefix,name,fig):
 p=next(ROOT.glob(prefix+'-*'))/'01-theory/algorithms/assets';p.mkdir(exist_ok=True,parents=True);fig.tight_layout(pad=1.6);fig.savefig(p/name,dpi=145,bbox_inches='tight');plt.close(fig)
t=np.arange(100);trend=50+.2*t+.4*np.maximum(0,t-50);season=5*np.sin(2*np.pi*t/7);holiday=np.where(t==70,15,0)
f,axs=plt.subplots(4,1,figsize=(10,8),sharex=True)
for ax,y,title in zip(axs,[trend,season,holiday,trend+season+holiday],['Piecewise trend with an illustrative slope change','Weekly Fourier component','One specified event contribution','Additive component prediction']):ax.plot(t,y,c=blue);ax.set(title=title,ylabel='Units')
axs[-1].set_xlabel('Time');f.suptitle('Component arithmetic illustration — not a fitted Prophet model',y=1.01);save('06','component-model.png',f)
f,axs=plt.subplots(3,1,figsize=(10,7));series=20+.2*t+4*np.sin(2*np.pi*t/7)
for ax,x,y,title in zip(axs,[t,t[1:],t[7:]],[series,np.diff(series),series[7:]-series[:-7]],['Original trend + weekly seasonality','Ordinary first difference','Weekly difference: repeat removed, trend remains constant']):ax.plot(x,y,c=blue);ax.set(title=title,ylabel='Units',xlabel='Time')
axs[2].set_ylim(1,1.8);axs[2].ticklabel_format(axis='y',style='plain',useOffset=False);save('06','difference-operators.png',f)
f,ax=plt.subplots(figsize=(9,4));periods=np.arange(21);croston=np.ones(21)*2;tsb=2*.9**periods;ax.plot(periods,croston,c=blue,label='Fixed Croston rate between positive events');ax.plot(periods,tsb,c=orange,label='TSB-style occurrence decay: size fixed, beta=.1');ax.set(title='Illustrative no-demand run after starting rate 2',xlabel='Consecutive zero periods',ylabel='Expected rate');ax.legend();save('06','intermittent-gap.png',f)
f,ax=plt.subplots(figsize=(9,4));x=np.linspace(5,16,400)
def density(x,mu,var):return np.exp(-(x-mu)**2/(2*var))/np.sqrt(2*np.pi*var)
for mu,var,label,col in [(10,4,'Prior state: mean 10, variance 4',blue),(12,1,'Observation likelihood: 12, noise variance 1',orange),(11.6,.8,'Updated state: mean 11.6, variance .8',green)]:ax.plot(x,density(x,mu,var),label=label,c=col)
ax.set(title='One scalar Kalman update combines two uncertain sources',xlabel='Latent state value',ylabel='Density');ax.legend(fontsize=9);save('06','kalman-update.png',f)
f,axs=plt.subplots(1,2,figsize=(11,4.5))
for ax,title,skip in zip(axs,['Plain path: repeated transformation','Residual path: identity plus learned correction'],[False,True]):
 ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1),title=title)
 for xpos,label in [(.1,'x'),(.5,'F(x)'),(.9,'output')]:ax.text(xpos,.45,label,ha='center',bbox=dict(fc='#dbeafe',ec='gray',boxstyle='round'))
 ax.annotate('',xy=(.39,.45),xytext=(.16,.45),arrowprops=dict(arrowstyle='->'));ax.annotate('',xy=(.8,.45),xytext=(.61,.45),arrowprops=dict(arrowstyle='->'))
 if skip:ax.annotate('',xy=(.87,.55),xytext=(.13,.55),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.45',color=orange));ax.text(.5,.85,'identity shortcut; output = x + F(x)',ha='center',fontsize=9)
save('05','residual-shortcut.png',f)
f,ax=plt.subplots(figsize=(9,4));c=np.arange(8,129,8);ax.plot(c,9*c*c,c=blue,label='Standard 3 x 3, C to C');ax.plot(c,9*c+c*c,c=orange,label='Depthwise 3 x 3 + pointwise, C to C');ax.set(title='Weight-count comparison, excluding biases — not a latency benchmark',xlabel='Channels C',ylabel='Weights');ax.legend();save('05','depthwise-weights.png',f)
f,ax=plt.subplots(figsize=(9,4));ax.bar(['Retained previous\n.8 x 2','Written candidate\n.1 x .5','Updated cell'],[1.6,.05,1.65],color=[blue,orange,green]);ax.set(title='One LSTM cell-state arithmetic example',ylabel='Cell-state contribution / value');save('05','lstm-cell-update.png',f)
print('Generated7new algorithm figures')
