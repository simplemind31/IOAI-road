import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
melbourne_data = pd.read_csv("melb_data.csv")
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
print(y)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X)
print(X.describe())
#melbourne_model = DecisionTreeRegressor(random_state=31)
# Fit model
#melbourne_model.fit(X, y)
#print("Making predictions for the following 5 houses:")
#print(X.head())
#print("The predictions are")
#prediction=melbourne_model.predict(X)
#print(mean_absolute_error(y,prediction))
train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=13)
melbourne_model=RandomForestRegressor(random_state=31)
melbourne_model.fit(train_X, train_y)
prediction=melbourne_model.predict(val_X)
print(mean_absolute_error(val_y,prediction))