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

data = open("u0plot.txt", 'r')
lines=data.readlines()
nu=[]
U_0=[]
dU_0=[]

for x in lines:
    nu.append(float(x.split()[0]))
    U_0.append(float(x.split()[1]))
    dU_0.append(float(x.split()[2]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title("Abhängigkeit Grenz-Gegenspannung von Frequenz des Lichts",
          y=1.08)
plt.xlabel("$\\nu/\mathrm{THz}$")
plt.ylabel("$U_0/\,\mathrm{V}$")

fit_params, pcov = scipy.optimize.curve_fit(f, nu, U_0, sigma=dU_0)


print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)
print(chi2(nu, U_0, dU_0, f, fit_params[0], fit_params[1]))

fitx = np.linspace(nu[0], nu[-1],num=10)
fity = f(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(nu, U_0, yerr = dU_0, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.68,0.25,  
            "Anpassung: $f(x)=\\alpha\cdot x +\\beta$\n $\\alpha=(%g \pm %g)\cdot 10^{-3}$ \n $\\beta=%g \pm %g$"%(round(fit_params[0]*1000,3), round(perr[0]*1000,3), round(fit_params[1],3),round(perr[1],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                    'alpha':0.7, 'pad':3})

# plt.ylim(U_0[-1]-0.5,U_0[0]+1)

plt.grid(True, zorder=0)

fig_U.savefig("u0plot.pdf")