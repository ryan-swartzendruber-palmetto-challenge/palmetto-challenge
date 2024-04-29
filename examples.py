import requests, json, duckdb
from usage_profile_example import get_usage_profile_example_response

api_root = 'https://api.genability.com'
profile_path = '/rest/v1/profiles'
account_path = '/rest/v1/accounts'

app_id = ''
app_key = ''

# response = requests.get(
#     f'{api_root}/rest/echo/hello', 
#     auth=(app_id, app_key),
#     data={},
#     headers={'content-type':'application/json'}
# )
# print(response)

# with open('./data/usage_profile.json', 'w') as usage_profile_file:
#     usage_profile_file.write(json.dumps(get_usage_profile_example_response()['results']))

sql = "SELECT SUM(readings.totalCount) FROM read_json('./data/*.json')"
print(duckdb.sql(sql))