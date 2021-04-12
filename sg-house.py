import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

house_data = pd.read_csv('hdb_resale_price_Aug2019.csv')
print(house_data.describe())
''' DATASET DETAILS 
Criteria used (coefficients of matrices):
floor_area_sqm
age
remaining_lease_years
---------------------
Output:
resale_price
'''
criteria = ['floor_area_sqm', 'age', 'remaining_lease_years']
town = input('Choose your town: ')
y = house_data[(house_data['town'] == (str(town)).upper())]['resale_price']
X = house_data[(house_data['town'] == (str(town)).upper())][criteria]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=20)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

print('Intercept: ', lm.intercept_)
print('Coefficients: \n', lm.coef_)

guess = []
for i in range(3):
  print('What is the ' + str(criteria[i]) + '?')
  x = float(input())
  guess.append(x)
est = lm.intercept_
for i in range(3):
  est += (guess[i]*lm.coef_[i])
print('Your estimated house price is ' + str(est))

predictions = lm.predict(X_test)

from sklearn import metrics
print()
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, predictions))
print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('Explained Variance Score: ', metrics.explained_variance_score(y_test, predictions))

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()
