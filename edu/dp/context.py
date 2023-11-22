from contextlib import contextmanager

@contextmanager
def timer():
    # Start the timer
    start = time.time()
    # context breakdown
    yield
    # End the timer
    end = time.time()

    # Tell the user how much time elapsed
    print(f"This code block executed in {round(end - start, 3)} seconds.")

import time

with timer():
    for _ in range(10):
        time.sleep(0.5)