# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from matplotlib.figure import Figure
from matplotlib.axes import Subplot

import matplotlib
# for convolve2d
import scipy.signal as sig

# <codecell>

from IPython.display import display, clear_output

# <codecell>

def paramtext(x,y,*args,**kwargs):

    paramstr='\n'.join(args)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    T=text(x,y,paramstr,
       ha='center',
       va='top',
       bbox=props,
       transform=gca().transAxes,
       multialignment='left',
       **kwargs)


# <codecell>

class Forest(object):

    def __init__(self,N=100,p=.01,f=.0001,g=0.0):
        self.neighborhood=ones((3,3))
        self.neighborhood[1,1]=0
        self.name="Forest Fire Simulation"
        self.p=p
        self.f=f
        self.N=N
        self.g=g

        self.field=zeros((self.N,self.N))
        self.image=[self.field]
        
    def reset(self):
        self.field=zeros((self.N,self.N))
        self.image=[self.field]
        
    def update(self):
                
        r=random.rand(self.N,self.N)
        r2=random.rand(self.N,self.N)
    
        empty=(self.field==0)
        trees=(self.field==1)
        burning=(self.field==2)
        
        s=sig.convolve2d(burning,self.neighborhood,mode='same')
    
        # grow a tree
        self.field[(r<self.p) & empty]=1
        
        # burning lasts only 1 cycle
        self.field[burning]=0

        # random extra burning
        r=random.rand(self.N,self.N)
        self.field[(r<self.f) & trees]=2
        
        # burn the neighborhood
        self.field[(s>0) & trees & (r2<(1.0-self.g))]=2
        
    def run(self):
        _fig=figure(figsize=(6,6))
        cmap=[ [0,0,0.0] , [0,1.0,0.0],[1.0,0,0]]
        my_cmap=matplotlib.colors.ListedColormap(cmap)
        ax=subplot(1,1,1)
        h=pcolor(f.field,cmap=my_cmap,vmin=0,vmax=2)

        paramtext(1.2,.9,
                  'p=%.4f' % f.p,
                  'f=%.4f' % f.f,
                  'g=%.4f' % f.g,
                  'N=%d' % f.N,
                  )

        axis('equal')
        i=0
        try:
            while True:
                clear_output(wait=True)
                h.set_array(f.field.ravel())
                title(str(i))
                i+=1
                f.update()
                display(_fig)
        except KeyboardInterrupt:
            pass
        

# <codecell>

f=Forest(N=100,
         p=.01,  # tree growing
         f=.00001,  # fire starting
         g=0.0)  # 1-p(neighbor burning)  g=0 ==> all neighbors
f.run()

# <codecell>


