import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split

sensitivity_score = recall_score
def specifity_score(y_true, y_pred):
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred)
    return r[0]

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'

X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)

model = LogisticRegression()
model.fit(X_train, y_train)

#y_pred = model.predict(X_test)

print(model.predict_proba(X_test))
y_pred = model.predict_proba(X_test)[:, 1] > 0.75

print("accuracy:", accuracy_score(y_test, y_pred))
print("precision:", precision_score(y_test, y_pred))
print("recall:", recall_score(y_test, y_pred))
print("f1 score:", f1_score(y_test, y_pred))

print("sensitivity:", sensitivity_score(y_test, y_pred))
print("specifity:", specifity_score(y_test, y_pred))
"""
print(model.score(X_test, y_test))

print("whole dataset:", X.shape, y.shape)
print("training set:", X_train.shape, y_train.shape)
print("test set:", X_test.shape, y_test.shape)

print("accuracy:", accuracy_score(y, y_pred))
print("precision:", precision_score(y, y_pred))
print("recall:", recall_score(y, y_pred))
print("f1 score:", f1_score(y, y_pred))
print(confusion_matrix(y, y_pred))

print((y == y_pred).sum())
print((y == y_pred).sum() / y.shape)
print(model.score(X, y))


#print(model.coef_, model.intercept_)

#print(model.predict(X[:50]))
#print(y[:50])

#print(X)
#print(y)

"""