from sklearn.model_selection import KFold
<<<<<<< HEAD
import pandas as pd
=======
import pandas as pd 
>>>>>>> ada2fc2e016914bec867920fc7a3c2449f1bcb5d

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
X = df[['Age', 'Fare']].values[:6]
y = df['Survived'].values[:6]

kf = KFold(n_splits=3, shuffle=True)
<<<<<<< HEAD

=======
>>>>>>> ada2fc2e016914bec867920fc7a3c2449f1bcb5d
for train, test in kf.split(X):
    print(train, test)