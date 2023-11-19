import requests

api_key = 'c0083e22-9489-499e-8cc6-1d51d4469058'
word = 'daisy'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)