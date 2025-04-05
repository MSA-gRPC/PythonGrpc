from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/processPayment", methods=["POST"])
def process_payment():
    data = request.get_json()
    card_number = data.get("card_number", "")
    amount = data.get("amount", 0.0)
    currency = data.get("currency", "")

    if card_number.startswith("1234"):
        response = {
            "success": True,
            "transaction_id": "1234",
            "message": f"Payment of {amount} {currency} processed successfully.",
            "server_note": "Thank you for your payment."
        }
    else:
        response = {
            "success": False,
            "transaction_id": "FAIL",
            "message": "Payment declined. Invalid card number.",
            "server_note": "No greeting available."
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)