import time
import grpc
from concurrent import futures
import payment_pb2
import payment_pb2_grpc

class PaymentServiceServicer(payment_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        if request.card_number.startswith("1234"):
            return payment_pb2.PaymentResponse(
                success=True,
                transaction_id="1234",
                message=f"Payment of {request.amount} {request.currency} processed successfully.",
                server_note="Thank you for your payment."
            )
        else:
            return payment_pb2.PaymentResponse(
                success=False,
                transaction_id="FAIL",
                message="Payment declined. Invalid card number.",
                server_note="Please verify your card details and try again."
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentServiceServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("PaymentService is running on port 50051.")
    try:
        while True:
            time.sleep(3600) 
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()