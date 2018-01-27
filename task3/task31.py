
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.lines as mlines
from scipy.interpolate import spline


df=pd.read_table('data.txt',sep=',',header=None)
df=df.T
df.columns=['Year','Suicide','Spending']

x=range(len(df.Year))

fig=plt.figure(figsize=(10,6))
ax0=fig.add_axes([0.1,0.1,0.75,0.6])

ax1=ax0.twinx()
ax2=ax1.twiny()

ax2.text(min(x)+0.8,12500,'US spending on science, space, and technology',color='r',fontsize=20)
ax2.text(min(x)+0.6,11500,'Suicides by hanging strangulation and suffocation',fontsize=20)
ax2.text(min(x)+4.8,12000,'correlates with',color='grey',fontsize=13)
ax2.text(min(x)+4,11000,'Correlation: 99.79%(r=0.99789126)',color='grey')

x_new=np.linspace(min(x),max(x)+0.1,300)
y_1=spline(x,df.Spending,x_new)
y_2=spline(x,df.Suicide,x_new)

ax0.plot(x_new[:-3],y_1[:-3],'r-')
ax2.plot(x_new[:-3],y_2[:-3],'k-')

ax0.plot(x,df.Spending,'rD')
ax2.plot(x,df.Suicide,'ko')
ax0.set_ylim(14,31)
ax2.set_ylim(4000,10001)

ax0.set_ylabel('US spending on science')
ax0.yaxis.label.set_color('red')
ax1.set_ylabel('Hanging suicides',rotation=-90)

ax0.set_ylim(15,30)
ax0.yaxis.grid()

ax0.yaxis.set_major_locator(mticker.FixedLocator(range(15,31,5)))
ax0.yaxis.set_major_formatter(mticker.FixedFormatter(['$%d billion'%i for i in range(15,31,5)]))
ax0.tick_params(axis='y',colors='red',length=0)

ax2.yaxis.set_major_locator(mticker.FixedLocator(range(4000,10001,2000)))
ax2.yaxis.set_major_formatter(mticker.FixedFormatter(['%d suicides'%i for i in range(4000,10001,2000)]))
ax1.tick_params(axis='y',length=0)
ax2.tick_params(axis='y',length=0)

ax0.set_xticks(np.linspace(min(x)-0.5,max(x)-0.5,11))
ax0.set_xticklabels([])
ax2.set_xticks(np.linspace(min(x)-0.5,max(x)-0.5,11))
ax2.set_xticklabels([])

for i in [3600,10200]:
    nlist=np.linspace(min(x)-0.25,max(x)-0.25,11)
    year=range(1999,2010)
    if i==3600:
        C='k'
    else:
        C='r'
    for j in range(len(nlist)):
        plt.text(nlist[j],i,'%d'%year[j],color=C)

legend1=mlines.Line2D([],[],color='r',marker='D',label='US spending on science')
legend2=mlines.Line2D([],[],color='k',marker='o',label='Hanging suicides')
Leg1=plt.legend(handles=[legend2],bbox_to_anchor=(0.5,-0.08))
ax = plt.gca().add_artist(Leg1)
plt.legend(handles=[legend1],bbox_to_anchor=(0.8,-0.08))

ax0.spines['left'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.savefig("task31.png")
plt.show()


