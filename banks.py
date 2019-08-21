import requests
from plaid import Client
from plaid.errors import APIError, ItemError

client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

# Provide the access token for the Item you want to remove
client.Item.remove(access_token)

response = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2017-01-09')
transactions = response['transactions']

# the transactions in the response are paginated, so make multiple calls while increasing the offset to
# retrieve all transactions
while len(transactions) < response['total_transactions']:
    response = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2017-01-09',
                                       offset=len(transactions)
                                      )
    transactions.extend(response['transactions'])


