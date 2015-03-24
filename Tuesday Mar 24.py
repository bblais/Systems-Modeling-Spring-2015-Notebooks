# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from science import *

# <codecell>

x=linspace(0,20,100)
y=0.1*x+3+randn(len(x))
plot(x,y,'o')

# <codecell>

def constant(x,a):
    return a

# <codecell>

model=MCMCModel(x,y,constant,
                a=Uniform(-10,10))
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <codecell>


