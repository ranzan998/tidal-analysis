tidal-analysis
Using csv data file having ocean current data at one location to find the tidal constituents.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pytides2.tide import Tide
from datetime import datetime
import matplotlib.dates as mdates


#file 1
df1 = pd.read_csv('/home/sci_lab/Desktop/shankar_test/process/with_jday/l1-492_txt.csv', index_col=0, parse_dates=True)
dates = [datetime(*x) for x in zip(df1['year'], df1['month'], df1['date'], df1['hour'], df1['min'])]

# the below csv file is created from the previous file1 by using tide.model commands, periods of the tidal constituents
# were taken a book.
df = pd.read_csv('/home/sci_lab/Desktop/constituent_amp_phase_per_l1-492_txt.csv')

#for df1
def components(df1):
    u_comp = df1.speed * np.cos(df1.direction)
    v_comp = df1.speed * np.sin(df1.direction)
    return u_comp,v_comp

u_comp, v_comp = components(df1)
demeaned = u_comp.values - u_comp.values.mean()
tide_decom = Tide.decompose(demeaned, dates)

from pandas import DataFrame
constituent = [c.name for c in tide_decom.model['constituent']]
df_constituent = DataFrame(tide_decom.model, index= constituent).drop('constituent', axis=1)

print(df_constituent.sort_values('amplitude', ascending=False))
exit
############################
import utide

time = mdates.date2num(dates)
coef = utide.solve(time, u_comp, v_comp, lat = 12, method='ols', conf_int='MC')

tide = utide.reconstruct(time, coef)
###############################


'''
first we create empty lists corresponding to each constituents,
'''
S2,R2,T2,K2,S1,P1,K1,L2,lambda2,Mf,mu2,nu2,N2,two_N2,MSF,Q1,two_Q1,M2,O1,M6,MN4,M3,MS4,S6,MK3,M1,M4, \
two_MK3,rho1,M8,S4, two_SM2,J1,OO1 = [[] for i in range(len(df.amplitude))]

list = [S2,R2,T2,K2,S1,P1,K1,L2,lambda2,Mf,mu2,nu2,N2,two_N2,MSF,Q1,two_Q1,M2,O1,M6,MN4,M3,MS4,S6,MK3,M1,M4, \
two_MK3,rho1,M8,S4, two_SM2,J1,OO1]

'''
The below loop is to create the series of the various constituents 
'''
for i in range(len(df.amplitude)):
    for j in range(len(df1.direction)):
        constituent = df['amplitude'][i] * np.sin((2*np.pi/(df['period'][i]*60))*(j*6) + df['phase'][i])
        list[i].append(constituent)

'''
this loop would add all the constituents at every time step which will give the value of our calculated tide.
'''
my_tide = []

for i in range(len(df1.direction)):
    sum = 0
    for j in range(5):
        sum = sum + list[j][i]
    my_tide.append(sum)

#########################################


fig, (ax6, ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(ncols=1, nrows=7, sharey=False, sharex=True)
ax6.vlines(200, -300,300)
ax5.vlines(200, -300,300)
ax4.vlines(200, -300,300)
ax3.vlines(200, -300,300)
ax2.vlines(200, -300,300)
ax1.vlines(200, -300,300)

ax0.plot(S2[0:1000], label="S2", color='green')
ax1.plot(R2[0:1000], label='R2', color ='red')
ax2.plot(T2[0:1000], label='T2', color ='blue')
ax3.plot(K2[0:1000], label='K2', color ='violet')
ax4.plot(S1[0:1000], label='S1', color ='orange')
ax5.plot(P1[0:1000], label='P1', color ='yellow')
ax6.plot(my_tide[0:1000], label='my_tide', color='black')

#print(np.corrcoef(tide.h,my_tide))
# result = 4.55459203e-04
fig.legend(bbox_to_anchor =(1.0, 0.55))
plt.show()
