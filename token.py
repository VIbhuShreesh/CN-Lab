def token_bucket(requests, rate, bucket_size):
    tokens = 0
    for i, req in enumerate(requests):
        tokens = min(bucket_size, tokens + rate)
        print(f"\nTime {i+1}: Tokens available: {tokens}")
        if req <= tokens:
            tokens -= req
            print(f"Accepted packet of size {req}")
        else:
            print(f"Packet of size {req} dropped")

token_bucket([1, 2, 5, 1, 3], rate=2, bucket_size=4)