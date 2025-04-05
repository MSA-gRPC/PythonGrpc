import requests

def run():
    url = "http://localhost:5000/processPayment"

    payload_success = {
        "card_number": "123456789", 
        "amount": 99.99,
        "currency": "USD"
    }

    response_success = requests.post(url, json=payload_success)

    payload_fail = {
        "card_number": "987654321",
        "amount": 50.00,
        "currency": "USD"
    }
    response_fail = requests.post(url, json=payload_fail)

    print("Success Response:", response_success.json())
    print("Failure Response:", response_fail.json())

if __name__ == "__main__":
    run()