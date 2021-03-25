"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def gaus(x,a,x0,stdev):
    return a*np.exp(-(x-x0)**2/(2*stdev**2))

def gaus2(x, a1, a2, x01, x02, stdev1, stdev2, offset):
    return gaus(x, a1, x01, stdev1)+gaus(x, a2, x02, stdev2)+offset

def gaus3(x, a1,a2,a3,x01,x02,x03,stdev1,stdev2,stdev3,offset):
    return gaus(x, a1, x01, stdev1)+gaus(x, a2, x02, stdev2)+gaus(x, a3, x03, stdev3)+offset

""" rot2 """

data = open("rot2.txt", 'r')
lines=data.readlines()
x=[]
y=[]
dy=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
data.close()

height1 = 100
height2 = 40
mean1 = -0.015
mean2 = 0.021
stdev1 = 0.01
stdev2 = 0.008
offset = y[0]

params = (height1,height2,mean1,mean2,stdev1,stdev2,offset)

fig_U = plt.figure(dpi=400)

plt.title("Isotopieaufspaltung der Balmer-Serie für Deuterium: $H_\\alpha$\n 1. Messung",
          y=1.08)
plt.xlabel("Winkel $\\omega_\\delta$")
plt.ylabel("Intensität $I$ in $\%$")

# fit_params, pcov = scipy.optimize.curve_fit(gaus, x, y, sigma=dy, p0=[95,-0.0125,0.04])

fit_params, pcov = scipy.optimize.curve_fit(gaus2, x, y, sigma=dy,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)
#print(chi2(x, y, dy, gaus2, fit_params[0], fit_params[1]))

fitx = np.linspace(x[0], x[-1],num=10000)
fity = gaus2(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.45,0.18,  
            "Anpassung: $f(x)=a_1\cdot \exp(-\\frac{(x-\\mu_1)^2}{2\\sigma_1^2})+a_2\exp(-\\frac{(x-\\mu_2)^2}{2\\sigma_2^2}) + c$\n $a_1=(%g \pm %g)$, $a_2=%g \pm %g$ \n $\\mu_1=(%g \pm %g)$, $\\mu_2=%g \pm %g$ \n$\\sigma_1=(%g \pm %g)$, $\\sigma_2=%g \pm %g$, $c=(%g \pm %g)$"%(round(fit_params[0],3),\
                                          round(perr[0],3), round(fit_params[1],3),\
                                              round(perr[1],3),round(fit_params[2],3),\
                                              round(perr[2],3),round(fit_params[3],3),\
                                              round(perr[3],3),round(fit_params[4],3),\
                                              round(perr[4],3),round(fit_params[5],3),\
                                              round(perr[5],3),round(fit_params[6],3),\
                                              round(perr[6],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 5,  
            bbox ={'facecolor':'white',  
                    'alpha':0.5, 'pad':1})


plt.xlim(-0.05,0.05)

plt.grid(True, zorder=0)

plt.tight_layout()

fig_U.savefig("rot2.pdf")


""" ROT3 """

data = open("rot3.txt", 'r')
lines=data.readlines()
x=[]
y=[]
dy=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
data.close()

height1 = 100
height2 = 40
mean1 = -0.015
mean2 = 0.021
stdev1 = 0.01
stdev2 = 0.008
offset = y[0]

params = (height1,height2,mean1,mean2,stdev1,stdev2,offset)

fig_U = plt.figure(dpi=400)

plt.title("Isotopieaufspaltung der Balmer-Serie für Deuterium: $H_\\alpha$\n 2. Messung",
          y=1.08)
plt.xlabel("Winkel $\\omega_\\delta$")
plt.ylabel("Intensität $I$ in $\%$")

fit_params, pcov = scipy.optimize.curve_fit(gaus2, x, y, sigma=dy,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitx = np.linspace(x[0], x[-1],num=10000)
fity = gaus2(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.45,0.18,  
            "Anpassung: $f(x)=a_1\cdot \exp(-\\frac{(x-\\mu_1)^2}{2\\sigma_1^2})+a_2\exp(-\\frac{(x-\\mu_2)^2}{2\\sigma_2^2}) + c$\n $a_1=(%g \pm %g)$, $a_2=%g \pm %g$ \n $\\mu_1=(%g \pm %g)$, $\\mu_2=%g \pm %g$ \n$\\sigma_1=(%g \pm %g)$, $\\sigma_2=%g \pm %g$, $c=(%g \pm %g)$"%(round(fit_params[0],3),\
                                          round(perr[0],3), round(fit_params[1],3),\
                                              round(perr[1],3),round(fit_params[2],3),\
                                              round(perr[2],3),round(fit_params[3],3),\
                                              round(perr[3],3),round(fit_params[4],3),\
                                              round(perr[4],3),round(fit_params[5],3),\
                                              round(perr[5],3),round(fit_params[6],3),\
                                              round(perr[6],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 5,  
            bbox ={'facecolor':'white',  
                    'alpha':0.5, 'pad':1})


plt.xlim(-0.05,0.05)

plt.grid(True, zorder=0)

plt.tight_layout()

fig_U.savefig("rot3.pdf")

""" TUERKIS """

data = open("tuerkis.txt", 'r')
lines=data.readlines()
x=[]
y=[]
dy=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
data.close()

height1 = 97
height2 = 48
mean1 = -0.02
mean2 = 0.002
stdev1 = 0.01
stdev2 = 0.01
offset = y[0]

params = (height1,height2,mean1,mean2,stdev1,stdev2,offset)

fig_U = plt.figure(dpi=400)

plt.title("Isotopieaufspaltung der Balmer-Serie für Deuterium: $H_\\beta$",
          y=1.08)
plt.xlabel("Winkel $\\omega_\\delta$")
plt.ylabel("Intensität $I$ in $\%$")

# fit_params, pcov = scipy.optimize.curve_fit(gaus, x, y, sigma=dy, p0=[95,-0.0125,0.04])

fit_params, pcov = scipy.optimize.curve_fit(gaus2, x, y, sigma=dy,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)
#print(chi2(x, y, dy, gaus2, fit_params[0], fit_params[1]))

fitx = np.linspace(x[0], x[-1],num=10000)
fity = gaus2(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.47,0.18,  
            "Anpassung: $f(x)=a_1\cdot \exp(-\\frac{(x-\\mu_1)^2}{2\\sigma_1^2})+a_2\exp(-\\frac{(x-\\mu_2)^2}{2\\sigma_2^2}) + c$\n $a_1=(%g \pm %g)$, $a_2=%g \pm %g$ \n $\\mu_1=(%g \pm %g)$, $\\mu_2=%g \pm %g$ \n$\\sigma_1=(%g \pm %g)$, $\\sigma_2=%g \pm %g$, $c=(%g \pm %g)$"%(round(fit_params[0],3),\
                                          round(perr[0],3), round(fit_params[1],3),\
                                              round(perr[1],3),round(fit_params[2],3),\
                                              round(perr[2],3),round(fit_params[3],3),\
                                              round(perr[3],3),round(fit_params[4],3),\
                                              round(perr[4],3),round(fit_params[5],3),\
                                              round(perr[5],3),round(fit_params[6],3),\
                                              round(perr[6],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 5,  
            bbox ={'facecolor':'white',  
                    'alpha':0.5, 'pad':1})


plt.xlim(-0.05,0.05)

plt.grid(True, zorder=0)

plt.tight_layout()

fig_U.savefig("tuerkis.pdf")

""" VIOLETT """

data = open("violett.txt", 'r')
lines=data.readlines()
x=[]
y=[]
dy=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
data.close()

height1 = 25
height2= 30
mean1 = 0.41
mean2 = 0.42
stdev1 = 0.0125
stdev2 = 0.0125
offset = y[0]

params = (height1,height2,mean1,mean2,
          stdev1,stdev2,offset)

fig_U = plt.figure(dpi=400)

plt.title("Isotopieaufspaltung der Balmer-Serie für Deuterium: $H_\\gamma$",
          y=1.08)
plt.xlabel("Winkel $\\omega_\\delta$")
plt.ylabel("Intensität $I$ in $\%$")

fit_params, pcov = scipy.optimize.curve_fit(gaus2, x[:950], y[:950], sigma=dy[:950],p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitx = np.linspace(x[950], x[0],num=10000)
fity = gaus2(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='b',
             markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messpunkte", zorder=10)

plt.legend(loc='best')
 
plt.figtext(0.54,0.18,  
            "Anpassung: $f(x)=a_1\cdot \exp(-\\frac{(x-\\mu_1)^2}{2\\sigma_1^2})+a_2\exp(-\\frac{(x-\\mu_2)^2}{2\\sigma_2^2}) + c$\n $a_1=(%g \pm %g)$, $a_2=%g \pm %g$ \n $\\mu_1=(%g \pm %g)$, $\\mu_2=%g \pm %g$ \n$\\sigma_1=(%g \pm %g)$, $\\sigma_2=%g \pm %g$, $c=(%g \pm %g)$"%(round(fit_params[0],3),\
                                          round(perr[0],3), round(fit_params[1],3),\
                                              round(perr[1],3),round(fit_params[2],3),\
                                              round(perr[2],3),round(fit_params[3],3),\
                                              round(perr[3],3),round(fit_params[4],3),\
                                              round(perr[4],3),round(fit_params[5],3),\
                                              round(perr[5],3),round(fit_params[6],3),\
                                              round(perr[6],3)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 5,  
            bbox ={'facecolor':'white',  
                    'alpha':0.5, 'pad':1})


plt.xlim(0.34,0.5)

plt.grid(True, zorder=0)

plt.tight_layout()

fig_U.savefig("violett.pdf")