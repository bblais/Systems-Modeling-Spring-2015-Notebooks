# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Lynx Hare Example

# <codecell>

import pandas
from pyndamics import *

# <codecell>

data=pandas.read_excel('data/lynx_hares.xlsx')

# <codecell>

data

# <codecell>

t_data=data['Year']
y_data=data['Hares']
x_data=data['Lynx']
plot(t_data,y_data,'-o')
plot(t_data,x_data,'-o')

# <markdowncell>

# the frequencies, and a bit of the magnitude is wrong here...needs to be fixed.

# <markdowncell>

# H is the Hare population, L is the Lynx population

# <codecell>


sim=Simulation()
sim.add("H'=a*H - b*H*L",30,plot=True)
sim.add("L'=c*H*L - d*L",4,plot=True)
sim.add_data(t=data['Year'],H=data['Hares'],plot=True)
sim.add_data(t=data['Year'],L=data['Lynx'],plot=True)
sim.params(a=.5,b=.02,c=.09,d=3)

sim.run(1900,1920)

# <codecell>

sim.mse('H')

# <codecell>

sim.mse('L')

# <codecell>


