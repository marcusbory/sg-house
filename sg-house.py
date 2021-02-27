import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

house_data = pd.read_csv('hdb_resale_price_Aug2019.csv')
print(house_data.describe())
''' DATASET DETAILS 
Metrics used (coefficients of matrices):
floor_area_sqm
age
remaining_lease_years
---------------------
Output:
resale_price
'''
metrics = ['floor_area_sqm', 'age', 'remaining_lease_years']
town = input('Choose your town: ')
y = house_data[(house_data['town'] == (str(town)).upper())]['resale_price']
X = house_data[(house_data['town'] == (str(town)).upper())][metrics]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=20)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

print('Coefficients: \n', lm.coef_)

guess = []
for i in range(3):
  print('What is the ' + str(metrics[i]) + '?')
  x = float(input())
  guess.append(x)
est = 0
for i in range(3):
  est += (guess[i]*lm.coef_[i])
print('Your estimated house price is ' + str(est))

predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()
