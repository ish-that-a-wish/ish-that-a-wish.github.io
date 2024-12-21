import requests
response = requests.get("api.ftcscout.org/graphql")
print(response.status_code)
print(response.json())