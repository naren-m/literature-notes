---
layout: "default"
title: "GetTransactionsFromMint"
word_count: 121
created: "2024-11-28T18:24:53.185076"
modified: "2024-11-28T18:24:53.185076"
---
# GetTransactionsFromMint


using mint 

```python
import requests

username = "your_username"
password = "your_password"

login_url = "https://wwws.mint.com/loginUserSubmit.xevent"
data = {"username": username, "password": password}

session = requests.Session()
session.post(login_url, data=data)

# Now that we're logged in, we can make requests to the various Mint endpoints
# to retrieve data about our accounts, transactions, etc.

# For example, to get a list of all our accounts:
accounts_url = "https://wwws.mint.com/getJsonData.xevent?task=transactions"
accounts_data = session.get(accounts_url).json()

print(accounts_data)

```
using plaid


- https://plaid.com/docs/api/
- https://plaid.com/docs/api/libraries/


```py
import plaid

client = plaid.Client(client_id='your_client_id', secret='your_secret', public_key='your_public_key', environment='sandbox')

response = client.Transactions.get(access_token,start_date='yyyy-mm-dd',end_date='yyyy-mm-dd')

print(response)

```