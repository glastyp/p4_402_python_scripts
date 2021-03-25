"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b):
    return a*x + b


def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i],a, b))/s[i])**2
    return chi

""" 1 """

data = open("405nm1.txt", 'r')
lines=data.readlines()
I=[]
dI=[]
U_G=[]
dU_G=[]

for x in lines:
    I.append(float(x.split()[0]))
    dI.append(float(x.split()[1]))
    U_G.append(float(x.split()[2]))
    dU_G.append(float(x.split()[3]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title("Kennlinie für $405\,\mathrm{nm}$; 1. Messung",
          y=1.08)
plt.xlabel("$U_\mathrm{G}/\,\mathrm{mV}$")
plt.ylabel("$\sqrt{I-I_0}/\,\sqrt{\mathrm{V}}$")

fit_params, pcov = scipy.optimize.curve_fit(f, U_G[:-6], I[:-6], sigma=dI[:-6])


print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)
print(chi2(U_G[:-6], I[:-6], dI[:-6], f, fit_params[0], fit_params[1]))

fitx = np.linspace(U_G[0], U_G[-1],num=10)
fity = f(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(U_G, I, xerr = dU_G, yerr = dI, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.68,0.579,  
            "Anpassung: $f(x)=a\cdot x +b$\n $a=(%g \pm %g)\cdot 10^{-3}$ \n $b=%g \pm %g$"%(round(fit_params[0]*1000,3), round(perr[0]*1000,3), round(fit_params[1],3),round(perr[1],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.ylim(I[-1]-1.5,I[0]+1)

plt.grid(True, zorder=0)

fig_U.savefig("405nm1.pdf")