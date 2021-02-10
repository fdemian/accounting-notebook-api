# Accounting notebook

## Implementation notes

The API was implemented on the tornado framework in python.
Modifying the configuration options allows the user to set an initial balance other than 0.
 

## How to run

- Run pipenv

´pipenv shell´

- Install packages

´pipenv sync´

- Run the application
 
 ´pipenv run main.py´

## API Implementation.

Below are some curl commands to test the 
api implementation.

### Transactions

GET (Fetch transactions history)

curl -H "Content-Type: application/json" -X GET http://localhost:8888/api/transactions

POST ( Commit new transaction to the account )

curl -d '{"type":"credit", "amount":"500"}' -H "Content-Type: application/json" -X POST http://localhost:8888/api/transactions
curl -d '{"type":"debit", "amount":"200"}' -H "Content-Type: application/json" -X POST http://localhost:8888/api/transactions

### Transaction 
GET (Find transaction by ID)

curl -H "Content-Type: application/json" -X GET http://localhost:8888/api/transactions/<transactionId>

### Account balance

curl -H "Content-Type: application/json" -X GET http://localhost:8888/api/account
