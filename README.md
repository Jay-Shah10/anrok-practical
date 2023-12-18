# Anrok-practical
Practical for the Anrok and Stripe.

## Stripe: 
Craete an account with Stripe. This will be out main billing service. This system will be used to capture customer information and product information. 

* [Stripe API Guide](https://stripe.com/docs/api)
* [Authentication](https://stripe.com/docs/api/authentication)
* [Invoice](https://stripe.com/docs/api/invoices)
* [InvoiceItem](https://stripe.com/docs/api/invoiceitems)
* [Customer](https://stripe.com/docs/api/customers)
* [Product](https://stripe.com/docs/api/products)
* [Price](https://stripe.com/docs/api/prices)
* [Stripe documentation](https://stripe.com/docs/payments/checkout/taxes?tax-calculation=tax-rates)


## Anrok
Platform used to keep track of all sales taxes for all the products offered. Few things to make sure of here, Makes sure customer id and product ids are the same in both systems. 

* [Integration with Stripe Guide](https://help-center.anrok.com/hc/en-us/articles/17604840278675-Integrate-Anrok-Stripe)
* [Anrok API Guide](https://apidocs.anrok.com/#section/API-reference)
* [Anrok Tutorial](https://apidocs.anrok.com/tutorials/)


### Requirements: 
```
* Python3 3.9.6
* Stripe Library
```

## How to run: 
* Install python3 (version 3.9.6 was used). Create python enviroment. `python3 -m venev .venv`. 
* Install required libraries in requirements.txt `pip install requirements.txt`. 
* Make sure to have accounts with Stripe and Anrok, and get the api keys. Requires API in as environment variables.`SK_TEST` and `ANROK_API_KEY`


## What it does: 
1. Creates an invoice for a specific customer (you will need to create a customer in Stripe and in Anrok and use that customer id).
2. Updates the invoice by creating invoice item. 
3. Creates an EphemeralTransaction in Anrok.
4. Finalized the invoice.
5. Updates / creates a transaction in Anrok.


