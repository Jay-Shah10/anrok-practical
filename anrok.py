import sys
import os
import json
import datetime

import requests


anroke_api_url = "https://api.anrok.com"
anrok_api_key = os.getenv("ANROK_API_KEY")
anrok_headers = {
    "Authorization": f"Bearer {anrok_api_key}",
    "Content-Type": "application/json",
}


def anrokCreateEphemeralTransaction(
    amount,
    city,
    currency_code,
    customer_id,
    country,
    line1,
    product_id,
    state,
    zipCode,
    line2=None,
):
    url = anroke_api_url + "/v1/seller/transactions/createEphemeral"
    data = {
        "currencyCode": currency_code,
        "accountingTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "accountingTimeZone": "UTC",
        "lineItems": [
            {"id": product_id, "productExternalId": product_id, "amount": amount}
        ],
        "customerId":customer_id,
        "customerAddress": {
            "country": country,
            "line1": line1,
            "city": city,
            "state": state,
            "zipCode": zipCode,
        },
    }
    payload = json.dumps(data)
    response = requests.post(url=url, data=payload, headers=anrok_headers)
    if response.status_code != 200:
        print(response.content)
    else:
        return response.content


def anrokUpdateTransaction(
    amount,
    city,
    country,
    currency_code,
    customer_id,
    invoice_id,
    line1,
    product_id,
    state,
    zipCode,
    line2=None,
):
    url = anroke_api_url + "/v1/seller/transactions/createOrUpdate"
    data = {
        "id": invoice_id,
        "currencyCode": currency_code,
        "accountingTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "accountingTimeZone": "UTC",
        "lineItems": [
            {"id": product_id, "productExternalId": product_id, "amount": amount}
        ],
        "customerId": customer_id,
        "customerAddress": {
            "country": country,
            "line1": line1,
            "city": city,
            "state": state,
            "zipCode": zipCode,
        },
    }
    payload = json.dumps(data)
    print(data)
    response = requests.post(url=url, data=payload, headers=anrok_headers)
    if response != 200:
        print(response.content)
    else:
        return response.content
