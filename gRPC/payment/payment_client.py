import grpc

import payment_pb2
import payment_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = payment_pb2_grpc.PaymentServiceStub(channel)

    request_success = payment_pb2.PaymentRequest(
        card_number="123456789",
        amount=99.99,
        currency="USD"
    )
    
    response_success = stub.ProcessPayment(request_success)
    print("Payment response:", "Success" if response_success.success else "Failed")
    print("Transaction ID:", response_success.transaction_id)
    print("Message:", response_success.message)
    print("Server Note:", response_success.server_note)
    print() 

    request_fail = payment_pb2.PaymentRequest(
        card_number="987654321",
        amount=50.00,
        currency="USD"
    )

    response_fail = stub.ProcessPayment(request_fail)
    print("Payment response:", "Success" if response_fail.success else "Failed")
    print("Transaction ID:", response_fail.transaction_id)
    print("Message:", response_fail.message)
    print("Server Note:", response_fail.server_note)

if __name__ == '__main__':
    run()