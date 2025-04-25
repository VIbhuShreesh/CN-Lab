def stop_and_wait(frames):
    for i, frame in enumerate(frames):
        print(f"Sending frame {i}")
        print(f"Acknowledgment for frame {i} received\n")

stop_and_wait(["A", "B", "C"])

def go_back_n(window_size):
    for i in range(0, 10, window_size):
        print(f"Sending frames {i} to {i+window_size-1}")
        print("ACK lost! Resending all...\n")

go_back_n(3)


received = [True, False, True, True]

for i, ack in enumerate(received):
    if not ack:
        print(f"Frame {i} not acknowledged. Resending...")
    else:
        print(f"Frame {i} acknowledged.")