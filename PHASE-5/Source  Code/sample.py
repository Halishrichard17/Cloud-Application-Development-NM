import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://eu-gb.dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
API_KEY = "6NZgUAO90FAOvaPc-aMSH5Z3l-yfOJPNrSq8cYcGNEde"
token_response = requests.post('https://private.eu-gb.ml.cloud.ibm.com/ml/v4/deployments/ed3ae77c-3fa6-4ebb-9e37-f4d99de5823b/predictions?version=2021-05-01', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields":  ["index",
                                "having_IPhaving_IP_Address",
                                "URLURL_Length",
                                "Shortining_Service",
                                "having_At_Symbol",
                                "double_slash_redirecting",
                                "Prefix_Suffix",
                                "having_Sub_Domain",
                                "SSLfinal_State",
                                "Domain_registeration_length",
                                "Favicon",
                                "port",
                                "HTTPS_token",
                                "Request_URL",
                                "URL_of_Anchor",
                                "Links_in_tags",
                                "SFH",
                                "Submitting_to_email",
                                "Abnormal_URL",
                                "Redirect",
                                "on_mouseover",
                                "RightClick",
                                "popUpWidnow",
                                "Iframe",
                                "age_of_domain",
                                "DNSRecord",
                                "web_traffic",
                                "Page_Rank",
                                "Google_Index",
                                "Links_pointing_to_page",
                                "Statistical_report"], "values":
                                [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                ]
                     }]}

response_scoring = requests.post('https://private.eu-gb.ml.cloud.ibm.com/ml/v4/deployments/ed3ae77c-3fa6-4ebb-9e37-f4d99de5823b/predictions?version=2021-05-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())