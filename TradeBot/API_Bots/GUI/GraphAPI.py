import requests
import json

def run_query(query):
    headers = {'6AkHLL16LAz5QpZV': 'BQYfzxUeS1DwCGM1c1n9Lk7MHQojvs9g'}
    request = requests.post('https://graphql.bitquery.io', json={'query': query}, headers=headers)
    
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}. {}'.format(request.status_code.query))


query = json.dumps(open('BlockChains/BTC.json', 'w'))

result = run_query(query)
print('Result - {}'.format(result))