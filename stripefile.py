import sys
import os
import json
import requests
import stripe
stripe.api_key=os.getenv('SK_TEST')


def creatStripeCustomer(customer_name, customer_email):
    customer = stripe.Customer.create(
        name=customer_name,
        email=customer_email 
    )
    return customer    

def getProduct():
    product = stripe.Product.list()
    return product

def getProductPrice(product_price):
    price = stripe.Price.retrieve(product_price)
    return price


def createInvoice(customer_id):
    invoice = stripe.Invoice.create(customer=customer_id)
    return invoice

def createInvoiceItem(customer_id, price_id, invoice_id):
    invoice_item = stripe.InvoiceItem.create(
        customer=customer_id,
        price=price_id,
        invoice=invoice_id
    )
    return invoice_item

def finalizeInvoice(invoice):
    finalizedInvoice = stripe.Invoice.finalize_invoice(invoice.id)
    return finalizedInvoice