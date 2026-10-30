"""Neural gradients, convolution and attention arithmetic. Local synthetic teaching example; Python3.10+ standard library."""
import math
x=2.;w=.1;b=0.;y=1.;p=1/(1+math.exp(-(w*x+b)))
old_loss=-math.log(p);gw=(p-y)*x;gb=p-y
w-=.1*gw;b-=.1*gb;newp=1/(1+math.exp(-(w*x+b)))
assert -math.log(newp)<old_loss
# A 1D cross-correlation convention, commonly called convolution in neural libraries.
signal=[1,2,3,4];kernel=[1,-1];output=[sum(signal[i+j]*kernel[j] for j in range(2)) for i in range(3)]
assert output==[-1,-1,-1]
logits=[0,math.log(3)];exps=[math.exp(z-max(logits)) for z in logits];weights=[v/sum(exps) for v in exps]
attention=sum(a*v for a,v in zip(weights,[2,6]));assert math.isclose(attention,5)
print('Neuron probability:',round(p,6),'->',round(newp,6),'convolution:',output,'attention:',attention)
