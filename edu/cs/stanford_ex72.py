# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_seq_items', None)
 
#%config InlineBackend.figure_formats = {'pdf',}
#%matplotlib inline

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')

img = plt.imread('F:\ML\machine-learning-ex7\machine-learning-ex7\ex7\\bird_small.png')
img_shape = img.shape
img_shape

A = img/255

AA = A.reshape(128*128,3)
AA.shape

km2 = KMeans(16)
km2.fit(AA)

B = km2.cluster_centers_[km2.labels_].reshape(img_shape[0], img_shape[1], 3)

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(13,9))
ax1.imshow(img)
ax1.set_title('Original')
ax2.imshow(B*255)
ax2.set_title('Compressed, with 16 colors')

for ax in fig.axes:
    ax.axis('off')

