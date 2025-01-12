# import sqlite3

# conn = sqlite3.connect("db.sqlite3")

# cur = conn.cursor()


# cur.execute("DELETE FROM gold_admin")
# conn.commit()
# conn.close()
import requests
import base64
def createApiUser():
      
      headers = {'Accept': '*/*',
                  'Content-Type': 'application/json',
                  'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500',
                  'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',}
      data={
            "providerCallbackHost": "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3"
            }
      r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser',json=data, headers = headers)
      print(r.json)
# createApiUser()

def GetApiUserInfo():
      headers = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',
      } 
      
      params={
            'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500'
      }
      
      r = requests.get('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/ae8231b8-d56a-4fa7-9e57-96fe55ee15cb',params=params,headers = headers)
      print(r.json())
# GetApiUserInfo()


def CreateApiKey():
      
      headers = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',
      }
      
      params={
            'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500'
      }
      
      r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/9e84a13a-b931-42b9-ad7b-64340411c500/apikey',headers = headers)
      print(r.text)
      
      {"apiKey":"b03c903926034ffcb76408582064da3d"}
# CreateApiKey()  


def generate_authorization(user, key):
    # Concatenate user and key with a colon
    auth_string = f"{user}:{key}"
    
    # Encode the string in Base64
    auth_bytes = auth_string.encode('utf-8')  # Convert to bytes
    auth_b64 = base64.b64encode(auth_bytes).decode()  # Encode and decode back to string
    
    return f"Basic {auth_b64}"

# Example usage:
user = "9e84a13a-b931-42b9-ad7b-64340411c500"
key = "b03c903926034ffcb76408582064da3d"
# authorization_value = generate_authorization(user, key)
# print("Authorization Header Value:", authorization_value)    

def CreateAccessToken():
      # user = "9e84a13a-b931-42b9-ad7b-64340411c500"
      # key = "b03c903926034ffcb76408582064da3d"
      # auth_string = f"{user}:{key}"
      # auth_b64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
      # athkey = f"Basic {auth_b64}"
      # print(athkey)
      headers = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
                 'Authorization': "Basic OWU4NGExM2EtYjkzMS00MmI5LWFkN2ItNjQzNDA0MTFjNTAwOmIwM2M5MDM5MjYwMzRmZmNiNzY0MDg1ODIwNjRkYTNk",
            #      "apiKey":"30dae6e8bb7743d7b7b186c413ad8569"
      }      
      r = requests.post('https://sandbox.momodeveloper.mtn.com/collection/token/', headers = headers)
      print(r.json())
      
      {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjllODRhMTNhLWI5MzEtNDJiOS1hZDdiLTY0MzQwNDExYzUwMCIsImV4cGlyZXMiOiIyMDI0LTEyLTEwVDE0OjM2OjEwLjAwNiIsInNlc3Npb25JZCI6IjJhNmU0MjljLTBkNTctNDY0Zi1hNjdmLWI4OTU5MzMyMzI3MyJ9.mos_AEtJDeQ9HMRJNdsXnsek2JU6Iavp8QeQOc1EL7BHsc4JTgnQvTC3-QqkmnHf09rZHI-z9kEfJQtQiJL4GcJv8Hgv7dFunN5RjpskAuUjA0ltRyeFTiFdDAt4ct4NZbSTITbRhRZ0GMlkgOlh_nKvCcWtKG4DpwEWHhUcU1SqJyAt6fHQSIOjbn-Q24GoQoqRG1R_Q2mFrWiV1KXNe6hCN_ALOUdLwoVNhP9G77nNJhc0EXTug7ZEdBrLSYMMxjbd74kzuubEOFyhkI-Bq-MLacQ4wQ1ZCiAHwBBvwIxjJG8XYspXmWKgOqynUi6nvBdEVDJ7Z6ddAf8abvFsxA', 'token_type': 'access_token', 'expires_in': 3600}
      
# CreateAccessToken()


def RequestToPay():
      accesToken = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjllODRhMTNhLWI5MzEtNDJiOS1hZDdiLTY0MzQwNDExYzUwMCIsImV4cGlyZXMiOiIyMDI0LTEyLTEwVDE0OjM2OjEwLjAwNiIsInNlc3Npb25JZCI6IjJhNmU0MjljLTBkNTctNDY0Zi1hNjdmLWI4OTU5MzMyMzI3MyJ9.mos_AEtJDeQ9HMRJNdsXnsek2JU6Iavp8QeQOc1EL7BHsc4JTgnQvTC3-QqkmnHf09rZHI-z9kEfJQtQiJL4GcJv8Hgv7dFunN5RjpskAuUjA0ltRyeFTiFdDAt4ct4NZbSTITbRhRZ0GMlkgOlh_nKvCcWtKG4DpwEWHhUcU1SqJyAt6fHQSIOjbn-Q24GoQoqRG1R_Q2mFrWiV1KXNe6hCN_ALOUdLwoVNhP9G77nNJhc0EXTug7ZEdBrLSYMMxjbd74kzuubEOFyhkI-Bq-MLacQ4wQ1ZCiAHwBBvwIxjJG8XYspXmWKgOqynUi6nvBdEVDJ7Z6ddAf8abvFsxA'
      headers = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
                 'Authorization': accesToken,
                 'X-Reference-Id': 'e2e84d62-f7b2-4dba-95c2-7797458ac9f6',  #THIS IS FORTHE TRASACTION NOT FOR THE CREATED USER 
            #      'X-Callback-Url': "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3",
                 'X-Target-Environment': "sandbox"
      }
      
      body={
            "amount": "10.0",
            "currency": "800",#code for UGX
            "externalId": "12345678",
            "payer": {
                  "partyIdType": "MSISDN",
                  "partyId": "12345678"
            },
            "payerMessage": "testing",
            "payeeNote": "testing1"
            }
      r = requests.post('https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay',json=body, headers = headers)

      print(r)
# RequestToPay()
def Get_payment_Status():
      accesToken = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjllODRhMTNhLWI5MzEtNDJiOS1hZDdiLTY0MzQwNDExYzUwMCIsImV4cGlyZXMiOiIyMDI0LTEyLTEwVDE0OjM2OjEwLjAwNiIsInNlc3Npb25JZCI6IjJhNmU0MjljLTBkNTctNDY0Zi1hNjdmLWI4OTU5MzMyMzI3MyJ9.mos_AEtJDeQ9HMRJNdsXnsek2JU6Iavp8QeQOc1EL7BHsc4JTgnQvTC3-QqkmnHf09rZHI-z9kEfJQtQiJL4GcJv8Hgv7dFunN5RjpskAuUjA0ltRyeFTiFdDAt4ct4NZbSTITbRhRZ0GMlkgOlh_nKvCcWtKG4DpwEWHhUcU1SqJyAt6fHQSIOjbn-Q24GoQoqRG1R_Q2mFrWiV1KXNe6hCN_ALOUdLwoVNhP9G77nNJhc0EXTug7ZEdBrLSYMMxjbd74kzuubEOFyhkI-Bq-MLacQ4wQ1ZCiAHwBBvwIxjJG8XYspXmWKgOqynUi6nvBdEVDJ7Z6ddAf8abvFsxA'
      headers = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
                 'Authorization': accesToken,
                 'X-Reference-Id': 'e2e84d62-f7b2-4dba-95c2-7797458ac9f6',  #THIS IS FORTHE TRASACTION NOT FOR THE CREATED USER 
            #      'X-Callback-Url': "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3",
                 'X-Target-Environment': "sandbox"
      }



# if request.user.is_authenticated:
#             name = request.user
#             customer = Customers.objects.get(username=name)
#             # cart_id = request.POST.get('cart_id')
#             # print(cart_id)
            
#             cart_object = Cart.objects.filter(cart_user_id=request.user.Customer_id)
#             print(cart_object)
            
#             orders = [
#                   Orders(
#                         order_user=customer,
#                         cart = item,
#                   ) for item in cart_object
#             ]
#             for item in cart_object:
#                   if Orders.objects.filter(cart=item):
#                         # orders.remove(item)
#                         print('items already exists')
#                   else:
#                         Orders.objects.bulk_create(orders)