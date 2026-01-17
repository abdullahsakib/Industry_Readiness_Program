
import time

class Timer:
    def __enter__(self):
        self.start=time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed=time.perf_counter()-self.start
        print(f"time taken {elapsed:.4f} seconds")


with Timer():
    for i in range(1_000_000):
        print(i)
        
    


