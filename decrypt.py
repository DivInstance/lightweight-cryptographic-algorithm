from src.lightcrypt import LightCrypt, generate_key, bytes_to_hex

def main():
    print("=== LightCrypt Decryption ===\n")
    
    encrypted_hex = input("Input Encrypted message : ")
    key_hex = input("Input the key : ")

    encrypted = bytes.fromhex(encrypted_hex)
    key = bytes.fromhex(key_hex)
    
    cipher = LightCrypt(key)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Encrypted: {bytes_to_hex(encrypted)}")
    print(f"Decrypted (Original Message): {decrypted.decode()}")
    
if __name__ == "__main__":
    main()

