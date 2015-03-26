# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from science import *

# <markdowncell>

# ## Anscombe’s quartet

# <codecell>

x1= array([ 10.,   8.,  13.,   9.,  11.,  14.,   6.,   4.,  12.,   7.,   5.])
y1= array([  8.04,   6.95,   7.58,   8.81,   8.33,   9.96,   7.24,   4.26,
        10.84,   4.82,   5.68])

x2= array([ 10.,   8.,  13.,   9.,  11.,  14.,   6.,   4.,  12.,   7.,   5.])
y2= array([ 9.14,  8.14,  8.74,  8.77,  9.26,  8.1 ,  6.13,  3.1 ,  9.13,
        7.26,  4.74])

x3= array([ 10.,   8.,  13.,   9.,  11.,  14.,   6.,   4.,  12.,   7.,   5.])
y3= array([  7.46,   6.77,  12.74,   7.11,   7.81,   8.84,   6.08,   5.39,
         8.15,   6.42,   5.73])

x4= array([  8.,   8.,   8.,   8.,   8.,   8.,   8.,  19.,   8.,   8.,   8.])
y4= array([  6.58,   5.76,   7.71,   8.84,   8.47,   7.04,   5.25,  12.5 ,
         5.56,   7.91,   6.89])

# <codecell>

print "Means:",mean(x1),mean(y1)
print "Standard Deviations:",std(x1),std(y1)

# <markdowncell>

# What are the means, etc... for the other data?

# <markdowncell>

# ## Visualizing and Fitting

# <codecell>

plot(x1,y1,'o')
result=fit(x1,y1,'linear')
print result

x=linspace(4,14,20)
y=fitval(result,x)
plot(x,y)
title(result['label'])

# <markdowncell>

# what does it look like for the other data?

# <codecell>


