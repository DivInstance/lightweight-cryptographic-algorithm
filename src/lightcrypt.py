"""
LightCrypt (LCA-128) - My Custom Lightweight Block Cipher
A simple 128-bit block cipher I built for learning cryptography.

Author: Divyaranjan Sahoo
Date: 31 August 
"""

import os

class LightCrypt:
    """Simple 128-bit block cipher using substitution-permutation network"""
    
    # My custom S-box (16 values for 4-bit substitution)
    SBOX = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
            0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
    
    # Reverse S-box for decryption
    INV_SBOX = [0] * 16
    for i in range(16):
        INV_SBOX[SBOX[i]] = i
    
    def __init__(self, key):
        """Initialize with 16-byte key"""
        if len(key) != 16:
            raise ValueError("Key must be 16 bytes")
        self.key = key
        self.round_keys = self._expand_key(key)
    
    def _expand_key(self, key):
        """Simple key expansion - generates 11 round keys"""
        # Convert key to integer for easier manipulation
        master_key = int.from_bytes(key, 'big')
        keys = [master_key]
        
        # Simple key schedule
        for i in range(10):
            # Rotate and XOR with round counter
            temp = keys[-1]
            temp = ((temp << 13) | (temp >> (128-13))) & ((1 << 128) - 1)
            temp ^= (i + 1) << 120  # Add round constant
            keys.append(temp)
        
        return keys
    
    def _substitute_bytes(self, state):
        """Apply S-box to each 4-bit nibble"""
        result = 0
        for i in range(32):  # 128 bits = 32 nibbles
            nibble = (state >> (4 * i)) & 0xF
            result |= self.SBOX[nibble] << (4 * i)
        return result
    
    def _inv_substitute_bytes(self, state):
        """Inverse S-box operation"""
        result = 0
        for i in range(32):
            nibble = (state >> (4 * i)) & 0xF
            result |= self.INV_SBOX[nibble] << (4 * i)
        return result
    
    def _permute_bits(self, state):
        """Simple bit permutation - just shift pattern"""
        # Simple permutation: shift each byte by its position
        result = 0
        for byte_pos in range(16):
            byte_val = (state >> (byte_pos * 8)) & 0xFF
            shift = (byte_pos * 3) % 8  # Different shift for each byte
            shifted = ((byte_val << shift) | (byte_val >> (8 - shift))) & 0xFF
            result |= shifted << (byte_pos * 8)
        return result
    
    def _inv_permute_bits(self, state):
        """Inverse permutation"""
        result = 0
        for byte_pos in range(16):
            byte_val = (state >> (byte_pos * 8)) & 0xFF
            shift = (byte_pos * 3) % 8
            shifted = ((byte_val >> shift) | (byte_val << (8 - shift))) & 0xFF
            result |= shifted << (byte_pos * 8)
        return result
    
    def encrypt_block(self, plaintext):
        """Encrypt single 16-byte block"""
        if len(plaintext) != 16:
            raise ValueError("Block must be 16 bytes")
        
        # Convert to integer
        state = int.from_bytes(plaintext, 'big')
        
        # Initial key addition
        state ^= self.round_keys[0]
        
        # 10 rounds of substitution and permutation
        for round_num in range(1, 11):
            state = self._substitute_bytes(state)
            state = self._permute_bits(state)
            state ^= self.round_keys[round_num]
        
        # Convert back to bytes
        return state.to_bytes(16, 'big')
    
    def decrypt_block(self, ciphertext):
        """Decrypt single 16-byte block"""
        if len(ciphertext) != 16:
            raise ValueError("Block must be 16 bytes")
        
        state = int.from_bytes(ciphertext, 'big')
        
        # Reverse the encryption
        for round_num in range(10, 0, -1):
            state ^= self.round_keys[round_num]
            state = self._inv_permute_bits(state)
            state = self._inv_substitute_bytes(state)
        
        # Final key addition
        state ^= self.round_keys[0]
        
        return state.to_bytes(16, 'big')
    
    def encrypt(self, plaintext):
        """Encrypt data with simple padding"""
        # Simple padding - add bytes with value of padding length
        pad_len = 16 - (len(plaintext) % 16)
        if pad_len == 0:
            pad_len = 16
        padded = plaintext + bytes([pad_len] * pad_len)
        
        # Encrypt each block
        result = b''
        for i in range(0, len(padded), 16):
            block = padded[i:i+16]
            result += self.encrypt_block(block)
        
        return result
    
    def decrypt(self, ciphertext):
        """Decrypt data and remove padding"""
        if len(ciphertext) % 16 != 0:
            raise ValueError("Invalid ciphertext length")
        
        # Decrypt each block
        result = b''
        for i in range(0, len(ciphertext), 16):
            block = ciphertext[i:i+16]
            result += self.decrypt_block(block)
        
        # Remove padding
        pad_len = result[-1]
        return result[:-pad_len]

# Simple utility functions
def generate_key():
    """Generate random 16-byte key"""
    return os.urandom(16)

def bytes_to_hex(data):
    """Convert bytes to hex string"""
    return data.hex().upper()

if __name__ == "__main__":
    # Simple test when run directly
    key = b"DivyaranjanSahoo"  # 16 bytes
    cipher = LightCrypt(key)
    
    message = b"Hello, World! This is my cipher."
    print(f"Original: {message}")
    
    encrypted = cipher.encrypt(message)
    print(f"Encrypted: {bytes_to_hex(encrypted)}")
    
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    
    print("Success!" if message == decrypted else "Failed!")