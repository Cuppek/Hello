from sklearn.model_selection import KFold
import pandas as pd 

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
X = df[['Age', 'Fare']].values[:6]
y = df['Survived'].values[:6]

kf = KFold(n_splits=7, shuffle=True)
for train, test in kf.split(X):
    print(train, test)