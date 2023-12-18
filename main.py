from anrok import anrokCreateEphemeralTransaction, anrokUpdateTransaction
from stripefile import createInvoice, createInvoiceItem, creatStripeCustomer, finalizeInvoice, getProduct, getProductPrice



def main():

    # walk thought: customer created (stripe)
    # Creating an invoice (stripe) --> create an ephemeral tranasction (anrok)
    # Finalize invoice (stripe) --> update or create transaction (anrok)
    
    # Barry Allen
    # customer_Id = "cus_PCQK7I58ct5Yo7"

    # # Bruce Wayne
    customer_Id = "cus_PCRbeKg6WJPNFV"

    stripe_product = getProduct()
    stripe_product_price = getProductPrice(stripe_product.data[0].default_price)

    invoice = createInvoice(customer_id=customer_Id)
    print(invoice.id)
    invoiceItem = createInvoiceItem(
        customer_id=customer_Id,
        price_id=stripe_product.data[0].default_price,
        invoice_id=invoice.id
    )

    anrokCreateEphemeralTransaction(
        amount=stripe_product_price.unit_amount,
        city=invoice.customer_address.city,
        currency_code=invoice.currency,
        customer_id=invoice.customer,
        country=invoice.customer_address.country,
        line1=invoice.customer_address.line1,
        product_id=stripe_product.data[0].id,
        state=invoice.customer_address.state,
        zipCode=invoice.customer_address.postal_code,
    )

    finazlied_invoice = finalizeInvoice(invoice=invoice)
    anrokUpdateTransaction(
        invoice_id=f'stripe:{invoice.id}',
        currency_code=invoice.currency,
        customer_id=invoice.customer,
        country=invoice.customer_address.country,
        line1=invoice.customer_address.line1,
        city=invoice.customer_address.city,
        state=invoice.customer_address.state,
        zipCode=invoice.customer_address.postal_code,
        product_id=stripe_product.data[0].id,
        amount=stripe_product_price.unit_amount
    )
    
    

if __name__ == "__main__":
    main()
