# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas
from pyndamics import *

# <codecell>

data=pandas.read_excel('data/s009.xls',skiprows=[0,1])

# <codecell>

data

# <codecell>

sim=Simulation()
sim.add("y'=slope",5,plot=True)
sim.params(slope=2)
sim.add_data(t=data['day'],y=data['height (cm)'],plot=True)
sim.run(0,90)

# <codecell>

sim.mse('y')

# <codecell>


