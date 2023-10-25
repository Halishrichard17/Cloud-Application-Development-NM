import xgboost as xgb
import pickle

import pandas as pd

data0 = pd.read_csv('dataset_website.csv')
X=data0.iloc[:,:31]
y=data0.iloc[:,31]
y = [0 if label == -1 else label for label in y]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)
X_train.shape, X_test.shape


model = xgb.XGBClassifier(
    learning_rate=0.1,
    n_estimators=100,
    max_depth=3,
    objective='binary:logistic'  # Adjust this for your problem
)

model.fit(X, y)

# Save the model to a file using pickle
with open('XGBoostClassifier.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("XGBoost model saved as xgboost_model.pkl")
