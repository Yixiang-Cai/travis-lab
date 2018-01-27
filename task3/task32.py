
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris=load_iris()
data=iris['data']
feature_names=iris['feature_names']
target=iris['target']
fig,ax=plt.subplots(4,4,figsize=(10,10))

for i in range(4):
    for j in range(4):
        if j==0:
            ax[i,j].set_ylabel(feature_names[i])
        else:
            ax[i,j].set_yticklabels([])
        if i==3:
            ax[i,j].set_xlabel(feature_names[j])
        else:
            ax[i,j].set_xticklabels([])
        if i==j:
            ax[i,i].hist(data[:,i],bins=20)
        else:
            ax[i,j].scatter(data[:,j],data[:,i],c=target,s=5,cmap='brg')
ax[0,0].set_yticks(np.linspace(1,15,7))
ax[0,0].set_yticklabels(np.linspace(4.5,7.5,7))
ax[1,0].set_yticks(np.linspace(2,4,5))
ax[2,0].set_yticks(range(1,8))
ax[3,0].set_yticks(np.linspace(0.5,2.5,5))
ax[3,0].set_xticks(np.linspace(4.5,7.5,7))
ax[3,0].tick_params('x',rotation=90.0)
ax[3,1].set_xticks(np.linspace(2,4,5))
ax[3,1].tick_params('x',rotation=90.0)
ax[3,2].set_xticks(range(1,8))
ax[3,2].tick_params('x',rotation=90.0)
ax[3,3].set_xticks(np.linspace(0.5,2.5,5))
ax[3,3].tick_params('x',rotation=90.0)

plt.subplots_adjust(wspace=0,hspace=0)

         
plt.show()
            
