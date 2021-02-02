import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from pylab import *
#plt.figure(figsize=(5,3))
#plt.style.use('style')
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#rc('font',**{'family':'serif','serif':['Times']})
#rc('text', usetex=True)

x0,y0 = np.loadtxt('no-soc.dat', unpack=True)
x,y,z,ztest = np.loadtxt('total.dat', unpack=True)
x1,y1,z1,z11 = np.loadtxt('Ga-s.dat', unpack=True) #Ga(s)
x2,y2,z2,z2x,z2y,z2z = np.loadtxt('Ga-p.dat', unpack=True) #Ga(p)
x3,y3,z3,z33 = np.loadtxt('As-s.dat', unpack=True) #As(s)
x4,y4,z4,z4x,z4y,z4z = np.loadtxt('As-p.dat', unpack=True) #As(p)
ef=-3.1982
y=y-ef
y0=y0-ef
x0=1+(x0*50.085589298)
kpts=[0,30,63,80]
labels = [r'$M$', r'$\Gamma$', r'$K$', r'$M$']
s=3 #marker size

subplot(2,3,1) #Ga(s) verde
colors1 = [(0,1,0,i) for i in np.linspace(0,1,100)]
cmap1 = mcolors.LinearSegmentedColormap.from_list('mycmap', colors1, N=100)
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x1,y, c=z1, cmap=cmap1,s=s)
#plt.colorbar()
plt.ylabel(r'$E-E_{VBM}$ (eV)')
plt.title(r'Ga ($s$)')
plt.xticks(kpts,['','','',''])
plt.xlim(0,80)
plt.ylim(-2,2)

subplot(2,3,2)#Ga(px,py) azul
colors2 = [(0,0,1,i) for i in np.linspace(0,1,100)]
cmap2 = mcolors.LinearSegmentedColormap.from_list('mycmap', colors2, N=100)
z2=z2x+z2y
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x2,y, c=z2, cmap=cmap2,s=s)
plt.title(r'Ga ($p_x+p_y$)')
plt.xticks(kpts,['','','',''])
plt.xlim(0,80)
plt.ylim(-2,2)

subplot(2,3,3)#Ga(pz) vermelho
colors3 = [(1,0,0,i) for i in np.linspace(0,1,100)]
cmap3 = mcolors.LinearSegmentedColormap.from_list('mycmap', colors3, N=100)
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x2,y, c=z2z, cmap=cmap3,s=s)
plt.title(r'Ga ($p_z$)')
plt.xticks(kpts,['','','',''])
plt.xlim(0,80)
plt.ylim(-2,2)

subplot(2,3,4)
plt.ylabel(r'$E-E_{VBM}$ (eV)')
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x,y, c=z3, cmap=cmap1,s=s)
plt.title(r'As ($s$)')
plt.xticks(kpts,labels)
plt.xlim(0,80)
plt.ylim(-2,2)

subplot(2,3,5)
z4=z4x+z4y
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x2,y, c=z4, cmap=cmap2,s=s)
plt.title(r'As ($p_x+p_y$)')
plt.xticks(kpts,labels)
plt.xlim(0,80)
plt.ylim(-2,2)

subplot(2,3,6)
plt.plot(x0,y0,'k-',lw=0.5)
plt.scatter(x2,y, c=z4z, cmap=cmap3,s=s)
plt.title(r'As ($p_z$)')
plt.xticks(kpts,labels)
plt.xlim(0,80)
plt.ylim(-2,2)

#subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.tight_layout()
plt.savefig('pBand.pdf',dpi=300)
