import xgboost as xgb
import pickle

import pandas as pd

data0 = pd.read_csv('dataset_website.csv')
X=data0.iloc[:,:31]
y=data0.iloc[:,31]
y = [0 if label == -1 else label for label in y]

from sklearn.preprocessing import LabelEncoder

#
# Step 2: Apply Label Encoding
encoder = LabelEncoder()

# Define a list of columns to be label-encoded
categorical_columns = ["index","having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","SSLfinal_State","Domain_registeration_length","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","Abnormal_URL","Redirect","on_mouseover","RightClick","popUpWidnow","Iframe","age_of_domain","DNSRecord","web_traffic","Page_Rank","Google_Index","Links_pointing_to_page","Statistical_report","Result"]

for column in categorical_columns:
    data0[column] = encoder.fit_transform(data0[column])

# Step 3: Save the encoded data to a new CSV file
data0.to_csv('encoded_data.csv', index=False)

print("Encoded data saved as encoded_data.csv")

