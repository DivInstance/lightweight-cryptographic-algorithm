# Lightweight Cryptography Algorithm ~ LightCrypt (LCA-128)

LightCrypt is a custom 128-bit encryption algorithm I built from scratch as my first project in learning cryptography. It's specifically designed for small, low-power devices like IoT sensors, smart home gadgets, and embedded systems that need to encrypt data but have limited processing power and battery life.

### Why LightCrypt?
Traditional encryption algorithms like AES can be too heavy for tiny devices. LightCrypt solves this by being:

1. **Lightweight**: Uses minimal memory and processing power
2. **Fast**: Optimized for quick encryption/decryption
3. **Secure**: Still provides strong data protection
---

### How It Works
LightCrypt uses a Substitution-Permutation Network (SPN) - a proven cryptographic structure that:

1. Substitutes data using lookup tables (adds confusion)
2. Permutes bits around (spreads changes across the data)
3. Repeats this process 10 times with different keys

**Technical Specs**
- Block Size: 128 bits (16 bytes at a time)
- Key Size: 128-bit encryption key
- Rounds: 10 cycles of substitution and permutation
- Structure: Substitution-Permutation Network (SPN)

Perfect for: IoT sensors, Arduino projects, battery-powered devices, and learning cryptography fundamentals.
---

### LightCrypt Architecture:
Plaintext (128 bits) → AddRoundKey → [SubBytes → ShiftRows → AddRoundKey] × 10 rounds → Ciphertext


---

### Key Concepts:
1. **Confusion**: Makes relationship between key and ciphertext complex (S-box)  
2. **Diffusion**: Spreads influence of single plaintext bit across many ciphertext bits (permutation)  
3. **Key Schedule**: Generates round keys from master key  
4. **Rounds**: Multiple iterations increase security  

---

## Project Structure
│── src/
│ └── lightcrypt.py # Core cipher implementation
│── demo/
│ └── demo.py # Example encryption/decryption usage
│── test/
│ └── test_lightcrypt.py # Unit tests (pytest)
│── benchmark/
│ ├── standard_benchmark.py # Benchmark LightCrypt only
│ └── compare_benchmark.py # Compare LightCrypt vs AES
|── encrypt.py
|── decrypt.py
│── README.md


---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/DivInstance/lightweight-cryptographic-algorithm
cd lightweight-cryptography-algorithm
pip install -r requirements.txt
```

##### Dependencies:
1. Python 3.11+
2. pytest for testing
3. pycryptodome for AES benchmark

## Usage

### Run Encryption/Decryption
From the project root directory:

```bash
python -m src.lightcrypt
```
Alter the message value to encrypt/decrypt in the main function your own message.

### Demo Script
Run the demo to see example encryption/decryption on IoT-style payloads:

```bash
python -m demo.demo
```

### Run Tests
Unit tests (pytest):

```bash
pytest -v
```

### Benchmarking

##### Benchmark LightCrypt vs AES-128:

```bash
python -m benchmark.compare_benchmark
```

Results (500 iterations, ECB mode)
###### LightCrypt (LCA-128):
  Encryption: 4.1924 sec (119.26 KB/s)
  Decryption: 4.2446 sec (117.80 KB/s)

###### AES-128 (ECB):
  Encryption: 0.0034 sec (146838.82 KB/s)
  Decryption: 0.0030 sec (165573.35 KB/s)
---
  

## Future Enhancements for LightCrypt

- **Raspberry Pi Optimization & IoT Testing** : Test LightCrypt on actual Raspberry Pi hardware to measure real-world IoT benchmarks.
- **Statistical Security Analysis & Randomness Testing**: Perform NIST tests and avalanche analysis to validate cryptographic security.
- **CBC Mode Implementation & Hardware Translation**: Add CBC mode and create a C version for microcontroller/Arduino deployment.  

## Acknowledgements / Credits

This is my **first project in cryptography**.   I built LightCrypt (LCA-128) to learn and understand the principles of block ciphers and secure coding.  

References and resources that helped in designing the Substitution–Permutation Network (SPN) structure:  
- Cryptography textbooks and online resources on SPN ciphers  
- Research papers on lightweight block ciphers for IoT and embedded systems  
- Practical examples of AES and other standard block ciphers

## License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---


