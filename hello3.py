from sklearn.model_selection import train_test_split

X = [[1, 1], [2, 2], [3, 3], [4, 4]]
y = [0, 0, 1, 1]

X_train, y_train, X_test, y_test = train_test_split(X, y)

print('X_train', X_train)
print('X_test', X_test)
print('X_test',y_train)
print('X_test', y_test)