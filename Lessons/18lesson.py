# JavaScript Object Notation (JSON)
import requests
from faker import Faker
import json


# In js we would do:
# axios.get('https://...')

URL = 'https://jsonplaceholder.typicode.com/todos/1'

# In python we do:
response = requests.get(URL)

# To get the status code:
print("status_code: ",response.status_code)

# To get the content:
print("content: ",response.content)

# To get the json:
print("json(): ",response.json())


# JSON.stringify(data)
# JSON.parse(data)

# stringify   [{...}, {...}, {...}]  =>  "..."
# parse       "..."   =>  [{...}, {...}, {...}]

# json.dumps(...)  =>  "..."
# json.loads(...)  =>  {...}

