import paypalrestsdk
import config

import logging

logging.basicConfig(level=logging.INFO)

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": config.ClientID,
  "client_secret": config.SecretID })

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "Sosi",
                "sku": "item",
                "price": "0.1",
                "currency": "RUB",
                "quantity": 1}]},
        "amount": {
            "total": "0.1",
            "currency": "RUB"},
        "description": "This is the payment transaction description."}]})

if payment.create():
    print("Payment[%s] created successfully" % (payment.id))
    # Redirect the user to given approval url
   # for link in payment.links:
       # if link.rel == "approval_url":
            # Convert to str to avoid google appengine unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
           # approval_url = str(link.href)
            ##print("Redirect for approval: %s" % (approval_url))
else:
    print("Error while creating payment:")
  #  print(payment.error)

print('###################################################################################')

if payment.execute({"payer_id": payment.id}):
  print("Payment execute successfully")
else:
  print(payment.error) # Error Hash