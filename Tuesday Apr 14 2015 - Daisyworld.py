# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pyndamics import *

# <codecell>

#constants
black_albedo = 0.25
uncovered_albedo = 0.5
white_albedo = 0.75

death_rate = 0.3
heat_absorp_fact = 20


# <codecell>

def growth(T,T_max=210.0,T_width=40.0):
    val=1-( (T_max-T )/(T_width/2) )**2
    if val<0.0:
        val=0.0
    return val

T=linspace(180,260,100)
y=[growth(_) for _ in T]
plot(T,y)

# <codecell>

def oscillation(t):
    return 1.0-0.60*sin(t/pi/10)

def ramp(t):
    return 0.2+0.004*t

t=linspace(0,400,100)
plot(t,oscillation(t))
plot(t,ramp(t))

# <codecell>


sim=Simulation()

sim.add("uncovered_area=1-black_area-white_area",1,plot=1)
sim.add("L=ramp(t)",1,plot=2)
sim.add("albedo=uncovered_area*uncovered_albedo + black_area*black_albedo + white_area*white_albedo",0.5,plot=3)
sim.add("global_temp=88.5*(S*L*(1-albedo))**.25",plot=4)
sim.add("global_temp_dead=88.5*(S*L*(1-uncovered_albedo))**.25",plot=4)
sim.add("black_local_temp=global_temp+q*(uncovered_albedo-black_albedo)",plot=4)
sim.add("white_local_temp=global_temp+q*(uncovered_albedo-white_albedo)",plot=4)

sim.add("black_growth=growth(black_local_temp)",plot=5)
sim.add("white_growth=growth(white_local_temp)",plot=5)



sim.add("black_area'=black_area*(uncovered_area*black_growth-gamma)+.001",0,plot=1)
sim.add("white_area'=white_area*(uncovered_area*white_growth-gamma)+.001",0,plot=1)

sim.params(black_albedo = 0.25,
            uncovered_albedo = 0.5,
            white_albedo = 0.75,
            gamma=0.3,
            S=65,
            q=40,
            )
sim.functions(oscillation,ramp,growth)
sim.run(0,600)

# <markdowncell>

# ## Some questions
# 
# 1. What happens when the $L$ is a ramp function as opposed to the oscillations?
# 2. What happens if you change the black albedo and/or the white albedo - does it make the global temperature more flat during the ramp, or less flat?  
# 3. Does it change the total uncovered area?
# 1. why do they alternate?  Under what conditions does this happen?  (use your own words)
# 2. all die at certain times - Under what conditions does this happen?
# 3. Can you make the modulation of the global temperature more dramatic? less dramatic?

# <markdowncell>

# ## Another scenario
# 
# What happens if we make the black/white daisy growth depend only on the *global* temperature?  We can do this by setting $q=0$.

# <codecell>


sim=Simulation()

sim.add("uncovered_area=1-black_area-white_area",1,plot=1)
sim.add("L=ramp(t)",1,plot=2)
sim.add("albedo=uncovered_area*uncovered_albedo + black_area*black_albedo + white_area*white_albedo",0.5,plot=3)
sim.add("global_temp=88.5*(S*L*(1-albedo))**.25",plot=4)
sim.add("global_temp_dead=88.5*(S*L*(1-uncovered_albedo))**.25",plot=4)
sim.add("black_local_temp=global_temp+q*(uncovered_albedo-black_albedo)",plot=4)
sim.add("white_local_temp=global_temp+q*(uncovered_albedo-white_albedo)",plot=4)

sim.add("black_growth=growth(black_local_temp)",plot=5)
sim.add("white_growth=growth(white_local_temp)",plot=5)



sim.add("black_area'=black_area*(uncovered_area*black_growth-gamma)+.001",0,plot=1)
sim.add("white_area'=white_area*(uncovered_area*white_growth-gamma)+.001",0,plot=1)

sim.params(black_albedo = 0.25,
            uncovered_albedo = 0.5,
            white_albedo = 0.75,
            gamma=0.3,
            S=65,
            q=.1,
            )
sim.functions(oscillation,ramp,growth)
sim.run(0,600)

# <markdowncell>

# Let's accentuate the albedos.

# <codecell>


sim=Simulation()

sim.add("uncovered_area=1-black_area-white_area",1,plot=1)
sim.add("L=ramp(t)",1,plot=2)
sim.add("albedo=uncovered_area*uncovered_albedo + black_area*black_albedo + white_area*white_albedo",0.5,plot=3)
sim.add("global_temp=88.5*(S*L*(1-albedo))**.25",plot=4)
sim.add("global_temp_dead=88.5*(S*L*(1-uncovered_albedo))**.25",plot=4)
sim.add("black_local_temp=global_temp+q*(uncovered_albedo-black_albedo)",plot=4)
sim.add("white_local_temp=global_temp+q*(uncovered_albedo-white_albedo)",plot=4)

sim.add("black_growth=growth(black_local_temp)",plot=5)
sim.add("white_growth=growth(white_local_temp)",plot=5)



#sim.add("black_area'=black_area*(uncovered_area*black_growth-gamma)+.001",0,plot=1)
sim.add("black_area'=0",0,plot=1)
sim.add("white_area'=white_area*(uncovered_area*white_growth-gamma)+.001",0,plot=1)

sim.params(black_albedo = 0.05,
            uncovered_albedo = 0.5,
            white_albedo = 0.95,
            gamma=0.3,
            S=65,
            q=.1,
            )
sim.functions(oscillation,ramp,growth)
sim.run(0,600)

# <codecell>


