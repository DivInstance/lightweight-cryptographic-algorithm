
"""
Simple benchmark for LightCrypt
Measures encryption and decryption speed
"""

import os
import time
from src.lightcrypt import LightCrypt, generate_key

def benchmark(cipher, data, iterations=1000):
    # Measure encryption
    start = time.time()
    for _ in range(iterations):
        cipher.encrypt(data)
    enc_time = time.time() - start

    # Measure decryption
    encrypted = cipher.encrypt(data)
    start = time.time()
    for _ in range(iterations):
        cipher.decrypt(encrypted)
    dec_time = time.time() - start

    print(f"Benchmark results ({iterations} iterations):")
    print(f"  Encryption: {enc_time:.4f} sec "
          f"({(len(data)*iterations/enc_time)/1024:.2f} KB/s)")
    print(f"  Decryption: {dec_time:.4f} sec "
          f"({(len(data)*iterations/dec_time)/1024:.2f} KB/s)")

if __name__ == "__main__":
    key = generate_key()
    cipher = LightCrypt(key)

    # Example: benchmark on 1 KB of random data
    data = os.urandom(1024)

    print("Running LightCrypt benchmark...")
    benchmark(cipher, data, iterations=500)
