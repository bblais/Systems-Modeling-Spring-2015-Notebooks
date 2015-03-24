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

# <markdowncell>

# ## Linear Model

# <codecell>

def linear(x,m,b):
    return m*x+b

# <codecell>

model=MCMCModel(x,y,linear,
                m=Uniform(-10,10),
                b=Uniform(-10,10),
                )
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <markdowncell>

# ## What happens if the true value is outside the prior?

# <codecell>

x=linspace(0,20,100)
y=5*x+30+4*randn(len(x))
plot(x,y,'o')

# <codecell>

model=MCMCModel(x,y,linear,
                m=Uniform(-10,10),
                b=Uniform(-10,10),
                )
model.run_mcmc(500)
model.plot_chains()

# <markdowncell>

# modify the range of the prior...

# <codecell>

model=MCMCModel(x,y,linear,
                m=Uniform(-10,10),
                b=Uniform(-100,100),   # <---- bigger range
                )
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <codecell>

model.triangle_plot()

# <codecell>

data=pandas.read_excel('data/sunflower.xls')

# <codecell>

data

# <codecell>

x=data['day']
y=data['height (cm)']
plot(x,y,'o')

# <codecell>

def constant(x,a):
    return a

# <codecell>

model=MCMCModel(x,y,constant,
                a=Uniform(-10,1000))
model.run_mcmc(500)
model.plot_chains()

# <codecell>

model.plot_distributions()

# <codecell>


