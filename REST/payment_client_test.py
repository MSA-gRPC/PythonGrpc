import requests
import time

def run_test(num_runs=10):

    url = "http://localhost:5000/processPayment"
    
    times = []

    for i in range(num_runs):
        payload = {
            "card_number": "123456789", 
            "amount": 99.99,
            "currency": "USD"
        }
        
        start_time = time.time()

        response = requests.post(url, json=payload)
        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)

        data = response.json()
        
        print(f"Run {i+1}:")
        print(f"  Payment response: {'Success' if data.get('success') else 'Failed'}")
        print(f"  Transaction ID: {data.get('transaction_id')}")
        print(f"  Message: {data.get('message')}")
        print(f"  Server Note: {data.get('server_note')}")
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