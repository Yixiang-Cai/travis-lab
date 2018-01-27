
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np

boston=load_boston()
data=boston.data
target=boston.target
feature_names=boston.feature_names

fig,ax=plt.subplots(3,5,figsize=(20,15))
for i in range(3):
    for j in range(5):
        try:
            if j!=0:
                ax[i,j].set_yticklabels([])
            ax[i,j].scatter(data[:,i*5+j],target,alpha=0.5)
            ax[i,j].set_xlabel(feature_names[i*5+j])
            ax[i,j].tick_params('x',rotation=90,labelsize=8)
        except:
            break
plt.subplots_adjust(wspace=0,hspace=0.4)
ax[0,0].set_ylabel('target MEDV')
ax[1,0].set_ylabel('target MEDV')
ax[2,0].set_ylabel('target MEDV')

ax[2,3].set_visible(False)
ax[2,4].set_visible(False)

plt.savefig("task33.png")
plt.show()

