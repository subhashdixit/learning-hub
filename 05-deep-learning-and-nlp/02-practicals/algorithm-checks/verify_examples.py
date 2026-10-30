"""Check the small worked calculations, not train every architecture. Standard library only."""
import math
# Perceptron representation limitation and a constructive hidden-layer XOR.
for a,b,target in [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]:
    assert int(a+b>.5)-int(a+b>1.5)==target
assert 8*(3*3*3+1)==224
assert 9*32*32==9216 and 9*32+32*32==1312
assert math.isclose(.8*2+.1*.5,1.65)
assert math.isclose(.5**20,9.5367431640625e-7)
weights=[1/4,3/4];assert sum(w*v for w,v in zip(weights,[2,6]))==5
assert 1024*8+8*1024==16384
assert math.isclose(math.sqrt(.64)*2+math.sqrt(1-.64)*1,2.2)
assert (2+4+6)/3==4
assert (224//16)**2==196 and 196**2==38416
# Forecasting examples cross-check their stated model conventions.
assert 2+.5*10==7 and 2+.5*7==5.5
assert math.isclose(100+4*sum(.8**i for i in range(1,6)),110.75712)
assert 100-10+25==115 and 200*(1-.1)+25==205
assert math.isclose(10+(4/(4+1))*(12-10),11.6)
assert math.isclose(10/5,2) and math.isclose((1-.2/2)*10/5,1.8)
assert math.isclose(.1+.2*4+.7*1,1.6)
assert math.isclose((1+1+2*.5)/4,.75)
print('Passed worked arithmetic checks for forecasting and deep-learning stories')
