import numpy as np
import pandas as pd
from collections import deque

# generate some data
# define features and target values
data = {
    'breathing_issues': ['Yes', 'No'],
    'fever': ['Yes', 'No'],
    'cough': ['Yes', 'No'],
    'fever_hoja': ['Yes', 'No']
}

# create an empty dataframe
data_df = pd.DataFrame(columns=data.keys())

np.random.seed(42)
# randomnly create 1000 instances
for i in range(1000):
    data_df.loc[i, 'breathing_issues'] = str(np.random.choice(data['breathing_issues'], 1)[0])
    data_df.loc[i, 'fever'] = str(np.random.choice(data['fever'], 1)[0])
    data_df.loc[i, 'cough'] = str(np.random.choice(data['cough'], 1)[0])
    data_df.loc[i, 'fever_hoja'] = str(np.random.choice(data['fever_hoja'], 1)[0])

data_df.head()

# separate target from predictors
X = np.array(data_df.drop('fever_hoja', axis=1).copy())
y = np.array(data_df['fever_hoja'].copy())
feature_names = list(data_df.keys())[:3]

# import and instantiate our DecisionTreeClassifier class
from ID3 import DecisionTreeClassifier

# instantiate DecisionTreeClassifier
tree_clf = DecisionTreeClassifier(X=X, feature_names=feature_names, labels=y)
print("System entropy {:.4f}".format(tree_clf.entropy))
# run algorithm id3 to build a tree
tree_clf.id3()
tree_clf.printTree()
