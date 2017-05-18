#Simple threshold value based classification. Doesn't always give the best result.
#Dataset used Iris DataSet

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
import warnings
warnings.filterwarnings("ignore",category=np.VisibleDeprecationWarning)

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']

#Just a random example
example = np.array([5.8,3.3,3.7,1.2])

##Use matplotlib to visualize the data and get some key observations##
for t,marker,c in zip(range(3),">ox","rgb"):
  plt.scatter(features[target == t,0],features[target == t,1],marker=marker,c=c)

plength = np.array(features[:,2])
is_setosa = (target_names=='setosa')
max_setosa = plength[is_setosa].max()
min_not_setosa = plength[~is_setosa].min()

if example[2]<max_setosa:
    print("Iris Setosa\n")
else:
    features = features[~is_setosa]
    labels = target_names[~is_setosa]
    virginica = (labels == 'virginica')

    best_acc = -1.0
    for fi in range(features.shape[1]):
        # We are going to generate all possible threshold for this feature
        thresh = features[:,fi].copy()
        thresh.sort()
        # Now test all thresholds:
        for t in thresh:
            pred = (features[:,fi] > t)
            acc = (pred == virginica).mean()
            if acc > best_acc:
                best_acc = acc
                best_fi = fi
                best_t = t
                if example[best_fi] > t:
                    print 'virginica'
                else:
                    print 'versicolor'
