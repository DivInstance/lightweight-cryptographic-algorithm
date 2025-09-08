from src.lightcrypt import LightCrypt, generate_key, bytes_to_hex

def main():
    print("=== LightCrypt Encryption ===\n")
    
    key = generate_key()
    print(f"Using key: {bytes_to_hex(key)}\n")

    cipher = LightCrypt(key)

    user_input = input("Input message for encryption: ")
    
    message = user_input.encode()
    encrypted = cipher.encrypt(message)
    
    print(f"Original:  {message}")
    print(f"Encrypted: {bytes_to_hex(encrypted)}")
    
if __name__ == "__main__":
    main()
