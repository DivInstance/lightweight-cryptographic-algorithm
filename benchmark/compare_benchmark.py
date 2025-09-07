"""
Benchmark: LightCrypt vs AES-128
"""

import os
import time
from src.lightcrypt import LightCrypt, generate_key
from Crypto.Cipher import AES

def benchmark_cipher(name, encrypt_fn, decrypt_fn, data, iterations=500):
    """Run simple benchmark on a cipher"""
    # Encrypt benchmark
    start = time.time()
    for _ in range(iterations):
        encrypt_fn(data)
    enc_time = time.time() - start

    # Decrypt benchmark
    encrypted = encrypt_fn(data)
    start = time.time()
    for _ in range(iterations):
        decrypt_fn(encrypted)
    dec_time = time.time() - start

    print(f"{name} ({iterations} iterations):")
    print(f"  Encryption: {enc_time:.4f} sec "
          f"({(len(data)*iterations/enc_time)/1024:.2f} KB/s)")
    print(f"  Decryption: {dec_time:.4f} sec "
          f"({(len(data)*iterations/dec_time)/1024:.2f} KB/s)")
    print("-" * 50)


if __name__ == "__main__":
    
    data = os.urandom(1024)

    # --- LightCrypt ---
    lc_key = generate_key()
    lc = LightCrypt(lc_key)
    benchmark_cipher(
        "LightCrypt (LCA-128)",
        lc.encrypt,
        lc.decrypt,
        data,
        iterations=500
    )

    # --- AES-128 (ECB mode) ---
    aes_key = os.urandom(16)
    aes = AES.new(aes_key, AES.MODE_ECB)

    def aes_encrypt(msg):

        pad_len = 16 - (len(msg) % 16)
        msg_padded = msg + bytes([pad_len] * pad_len)
        return aes.encrypt(msg_padded)

    def aes_decrypt(ct):
        pt = aes.decrypt(ct)
        pad_len = pt[-1]
        return pt[:-pad_len]

    benchmark_cipher(
        "AES-128 (ECB)",
        aes_encrypt,
        aes_decrypt,
        data,
        iterations=500
    )
