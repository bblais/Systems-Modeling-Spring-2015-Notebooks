# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Python For Data Analysis
# 
# 1. Loading Data
# 2. Trendlines
# 3. Statistical Analysis
# 4. Why Script?

# <codecell>

from science import *

# <markdowncell>

# http://data.giss.nasa.gov/gistemp/station_data/

# <codecell>

data=pandas.read_csv('temperature_data/johnstown.txt', delimiter=r"\s+")
data.head()

# <codecell>

year,temp=data['YEAR'],data['metANN']

# <codecell>

plot(year,temp,'-o')

# <codecell>

temp[temp>900]=NaN

# <codecell>

plot(year,temp,'-o')

# <codecell>

plot(year,temp,'-o')
xlabel('Year')
ylabel('Temperature (C)')

# <codecell>

def plot_temperature_data(fname):
    data=pandas.read_csv(fname, delimiter=r"\s+")
    
    year,temp=data['YEAR'],data['metANN']    
    temp[temp>900]=NaN
    
    figure()
    plot(year,temp,'-o')
    xlabel('Year')
    ylabel('Temperature (C)')    
    title(fname)

# <codecell>

from glob import glob
fnames=glob('temperature_data/*.txt')
for fname in fnames:
    plot_temperature_data(fname)

# <codecell>


