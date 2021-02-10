import json
from tornado.web import RequestHandler
from tornado.gen import coroutine
import datetime
import uuid

class TransactionsHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    # GET /transactions
    @coroutine
    def get(self):
        try:
            transactions = self.settings['transactions']

            self.set_status(200, 'Ok')
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(json.dumps(transactions))

        except E:

            response = {"message": e.mesage}

            self.set_status(500, 'Server Error')
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(json.dumps(response))

        return

    # POST /transactions
    def post(self):

        request = self.request.body.decode("utf-8")
        request_dict = json.loads(request)

        try:

          type = str(request_dict["type"])
          amount = int(request_dict["amount"])

          balance = self.settings['balance']

          if type == "debit":
              if balance-amount < 0:
                   response = { "message": "Transaction rejected. Account balance cannot be negative." }
                   self.set_status(400 , 'Bad Request')
                   self.set_header("Access-Control-Allow-Origin", "*")
                   self.write(json.dumps(response))
                   return
              else:
                  self.settings['balance'] = balance-amount
          else:
                 if type == "credit":
                     self.settings['balance'] = balance + amount

          current_date = datetime.datetime.now()
          trans_id = str(uuid.uuid4())
          trans_info = {
            "id": trans_id,
            "type": type,
            "amount": amount,
            "effectiveDate": str(current_date)
          }

          # Transacction successful. Append to the record of transactions.
          self.settings['transactions'].append(trans_info)

          self.set_status(201, 'Ok')
          self.set_header("Access-Control-Allow-Origin", "*")
          self.write(json.dumps(trans_info))

        except Exception as e :

            print(str(e))
            response = {"message": e}

            self.set_status(500, 'Server Error')
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(json.dumps(response))

        return

    @coroutine
    def put(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def delete(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def trace(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def connect(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def options(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def patch(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def head(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return


class TransactionHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    # GET /transactions/<transactionId >
    @coroutine
    def get(self, id):

        try:
           transactions = self.settings['transactions']

           for transaction in transactions:
               if transaction.id == id:
                   self.set_status(200, 'Ok')
                   self.set_header("Access-Control-Allow-Origin", "*")
                   self.write(json.dumps(transaction))
                   return


           response = { "Error": "Transaction not found." }
           self.set_status(404, 'Ok')
           self.set_header("Access-Control-Allow-Origin", "*")
           self.write(json.dumps(response))
           return

        except:
            response = {"Error": "An error has ocurred while retrieving the transaction."}
            self.set_status(500, 'Ok')
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(json.dumps(response))


    def post(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

        return


    @coroutine
    def put(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def delete(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def trace(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def connect(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def options(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def patch(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return

    @coroutine
    def head(self):
        response = {"message": "This is not a valid method for this resource."}
        self.set_status(405, 'Error')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)

        return
