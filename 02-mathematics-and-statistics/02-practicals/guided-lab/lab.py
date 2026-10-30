"""Statistics and probability calculations. Local synthetic teaching example; Python3.10+ standard library."""
import math,statistics,random
values=[2,4,6]
assert statistics.mean(values)==4 and statistics.variance(values)==4
prior=.01;sensitivity=.9;fpr=.05
posterior=sensitivity*prior/(sensitivity*prior+fpr*(1-prior))
assert math.isclose(posterior,90/585)
mean=50;sd=10;n=100;se=sd/math.sqrt(n);interval=(mean-1.96*se,mean+1.96*se)
assert interval==(48.04,51.96)
observed=[30,20,20,30];chi=sum((o-25)**2/25 for o in observed);assert chi==4
rng=random.Random(42);samples=[sum(rng.expovariate(1) for _ in range(30))/30 for _ in range(2000)]
assert abs(statistics.mean(samples)-1)<.05
print('Posterior:',round(posterior,6),'approximate CI:',interval,'chi-square:',chi)
print('Simulated mean of sample means:',round(statistics.mean(samples),4))
