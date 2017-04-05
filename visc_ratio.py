def ratio(h,l):
    return 6*(l*1.0/(2*math.pi*h))**3 #where h=debris thickness and l=arclength


import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
import math
import pylab
import numpy

#define limits
xmin = 1
xmax = 10
ymin = 1
ymax = 1000

#define grid
xx,yy=pylab.meshgrid(
    pylab.linspace(xmin,xmax,100),   #debris layer thickness, h
    pylab.linspace(ymin,ymax,300))   #arclength, l

# indexing of xx and yy (with the default value for the
# 'indexing' parameter of meshgrid(..) ) is as follows:
#
#   first index  (row index)    is y coordinate index
#   second index (column index) is x coordinate index
#
# as required by pcolor(..)

#fill matrix with visc ratio values
zz = pylab.zeros(xx.shape)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        zz[i,j] = ratio(xx[i,j],yy[i,j])

pylab.pcolor(xx,yy,zz,norm=LogNorm(vmin=zz.min(), vmax=zz.max()),cmap='afmhot') #logarithmic colourbar
pylab.colorbar(label=r'Viscosity Ratio $\frac{\mu_1}{\mu_m}$')


pylab.xlim([xmin,xmax])
pylab.ylim([ymin,ymax])

pylab.xlabel('Overburden Thickness (m)',fontsize=16,fontweight='bold')
pylab.ylabel('Ridge Arclength (m)',fontsize=16,fontweight='bold')

#Adding lines bounding the terrestrial viscosity ratios (order of magnitude, not precise values)

y1 = xx*2*math.pi*(1.0/6)**(1.0/3) #y values where viscosity ratio is equal to 1
y2 = xx*2*math.pi*(100.0/6)**(1.0/3) #y values where viscosity ratio is equal to 100

plt.semilogy(xx,y1,'k-',lw=3)
plt.hold(True)
plt.plot(xx,y2,'k-',lw=3)

#Put text on the plot where the terrestrial regime is
ax = plt.gca()
ax.text(6.15,63,'Terrestrial Regime',fontsize=16,fontweight='bold')

#Plot results from Tempe Terra, where L=586 m
plt.plot([xmin, xmax],[586, 586],'b--',lw=3)
ax.text(1.5,650,'Tempe Terra',fontsize=15,fontweight='bold',color='blue')

#Plot results from Deuteronilus Mensae, where arclength = 30.8
plt.plot([xmin, xmax],[30.8, 30.8],'w--',lw=3)
ax.text(2.1,23,'Deuteronilus Mensae',fontsize=15,fontweight='bold',color='white')

#Plot results from eastern Hellas, where arclength = 53
plt.plot([xmin, xmax],[53, 53],'m--',lw=3)
ax.text(1.05,60,'Eastern Hellas',fontsize=15,fontweight='bold',color='magenta')



pylab.show()
pylab.savefig('buckle_results.eps')
pylab.savefig('buckle_results.png')

