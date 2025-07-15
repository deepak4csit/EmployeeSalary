from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegressionCV

data = datasets.load_iris()

X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=40, test_size=.3)

