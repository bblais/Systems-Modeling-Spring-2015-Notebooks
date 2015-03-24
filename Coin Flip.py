# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from science import *
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

from IPython.html.widgets import interactive,ButtonWidget
from IPython.display import display

# <markdowncell>

# ## Some Simple Coin Flip Data

# <markdowncell>

# make up some data from an unfair coin

# <codecell>

p_true=pi/10  # just to make it interesting 0.314159
flips=rand(1000)<p_true

N=5
h=sum(flips[:N])
print h,N

# <codecell>

s=''.join(['H' if _ else 'T' for _ in flips])
print s

# <codecell>

def posterior(theta,h,N):
    return D.beta(a=h+1,b=(N-h)+1).pdf(theta)

def best_estimate(h,N):
    rv=D.beta(a=h+1,b=(N-h)+1)
    return rv.ppf(0.025),rv.ppf(0.5),rv.ppf(0.975)

# <codecell>

def plot_distribution(N=0):
    h=sum(flips[:N])
    figure(figsize=(16,5))
    x=linspace(0,1,300)
    y=posterior(x,h,N)
    plot(x,y)
    xlabel(r'$\theta$')
    ylabel(r'$p(\theta|h=%d,N=%d)$' % (h,N))

    est=best_estimate(h,N)
    gca().axvline(est[1])
    gca().axvline(p_true,color='r')

    label=r'\theta'
    v=est
    title(r'$\hat{%s}^{97.5}_{2.5}=%.3f^{+%.3f}_{-%.3f}$' % (label,v[1],(v[2]-v[1]),(v[1]-v[0])))


    fill_between_values=[est[0],est[2]]
    if fill_between_values:
        q=fill_between_values[0]
        idx=where(x<q)[0]
        try:
            imin=idx[-1]
        except IndexError:
            imin=0

        q=fill_between_values[1]
        idx=where(x<q)[0]
        imax=idx[-1]

        xf=concatenate(((x[imin],),x[imin:imax],(x[imax],)))
        yf=concatenate(((0,),y[imin:imax],(0,)))

        fill(xf,yf,facecolor='green', alpha=0.2)

    flipstr=''
    for i,c in enumerate(s[:N]):
        flipstr+=c
        if (i+1)%120==0:
            flipstr+='\n'
    
    paramtext(.5,-.2,'flips=%s' % flipstr,fontsize=12)

# <codecell>

plot_distribution(N)

# <codecell>

w=interactive(plot_distribution,
         N=(0,len(flips)),
         )
display(w)

# <markdowncell>

# ## Try an MCMC simulation

# <codecell>

def lnprob(theta):
    return D.beta(a=h+1,b=(N-h)+1).logpdf(theta)

# <codecell>

N=8
h=sum(flips[:N])

# <codecell>

ndim, nwalkers = 1, 100
pos=rand(100,1)
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob)

# <codecell>

timeit(reset=True)
print("Running MCMC...")
sampler.run_mcmc(pos, 150)
print("Done.")
print timeit()

# <codecell>

plot(sampler.chain[:, :, 0].T, color="k", alpha=0.4)
ax=gca()
ax.set_ylabel(r"$\theta$")

# <codecell>

y=sampler.chain[:, 50:, 0].ravel()
result=histogram(y,300)

# <codecell>


