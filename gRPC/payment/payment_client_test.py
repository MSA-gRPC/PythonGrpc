import grpc
import time
import payment_pb2
import payment_pb2_grpc

def run_test(num_runs=10):
    channel = grpc.insecure_channel('localhost:50051')
    stub = payment_pb2_grpc.PaymentServiceStub(channel)

    times = []

    for i in range(num_runs):
        request = payment_pb2.PaymentRequest(
            card_number="123456789", 
            amount=99.99,
            currency="USD"
        )
        
        start_time = time.time()
        response = stub.ProcessPayment(request)
        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)
        
        print(f"Run {i+1}:")
        print(f"  Payment response: {'Success' if response.success else 'Failed'}")
        print(f"  Transaction ID: {response.transaction_id}")
        print(f"  Message: {response.message}")
        print(f"  Server Note: {response.server_note}")
        print(f"  Time taken: {duration:.3f} seconds")
        print("-" * 40)

        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
    
        print("Summary:")
        print(f"  Average time: {avg_time:.3f} seconds")
        print(f"  Minimum time: {min_time:.3f} seconds")
        print(f"  Maximum time: {max_time:.3f} seconds")


if __name__ == '__main__':
    run_test(10)