"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b):
    return a*x+b


def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i],a, b))/s[i])**2
    return chi

""" 1 """

data = open("Balmer1.txt", 'r')
lines=data.readlines()
x=[]
y=[]
dy=[]
# dx=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
#    dU_G.append(float(x.split()[3]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title("Spektrallinien der Hg-Lampe",
          y=1.08)
plt.xlabel("$\\lambda/\mathrm{nm}$")
plt.ylabel("$\sin(\\alpha)+\sin(\\beta)$")

fit_params, pcov = scipy.optimize.curve_fit(f, x, y, sigma=dy)


print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)
print(chi2(x, y, dy, f, fit_params[0], fit_params[1]))

fitx = np.linspace(x[0], x[-1],num=10)
fity = f(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.7,0.2,  
            "Anpassung: $f(x)=a\cdot x +b$\n $a=(%g \pm %g)$ \n $b=%g \pm %g$"%(round(fit_params[0],3), round(perr[0],3), round(fit_params[1],3),round(perr[1],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})


#plt.ylim(y[-1]-1.5,y[0]+1)

plt.grid(True, zorder=0)

fig_U.savefig("Balmer1.pdf")