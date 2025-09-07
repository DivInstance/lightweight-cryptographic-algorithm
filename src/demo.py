"""
Simple demo of my LightCrypt cipher
Shows basic usage with different types of data
"""

from src.lightcrypt import LightCrypt, generate_key, bytes_to_hex
import json

def main():
    print("=== My LightCrypt Demo ===\n")
    
    key = generate_key()
    print(f"Using key: {bytes_to_hex(key)}\n")

    cipher = LightCrypt(key)
    
    # Test 1: Simple message
    print("Test 1: Simple Message")
    message = b"Do I like cats more or dogs"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Original:  {message}")
    print(f"Encrypted: {bytes_to_hex(encrypted)}")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {'Yes' if message == decrypted else 'No'}\n")
    
    # Test 2: IoT sensor data
    print("Test 2: IoT Sensor Data")
    sensor_data = {
        "device": "temp_sensor_01",
        "temperature": 23.5,
        "humidity": 60.2,
        "timestamp": 1234567890
    }
    
    json_data = json.dumps(sensor_data).encode('utf-8')
    encrypted = cipher.encrypt(json_data)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Original JSON: {json_data}")
    print(f"Encrypted size: {len(encrypted)} bytes")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {'Yes' if json_data == decrypted else 'No'}\n")
    
    # Test 3: Different key = different result
    print("Test 3: Different Keys")
    message = b"Same message"
    
    key1 = b"Key1234567890123"
    key2 = b"Key1234567890124" 
    
    cipher1 = LightCrypt(key1)
    cipher2 = LightCrypt(key2)
    
    encrypted1 = cipher1.encrypt(message)
    encrypted2 = cipher2.encrypt(message)
    
    print(f"Message: {message}")
    print(f"Key1 result: {bytes_to_hex(encrypted1)}")
    print(f"Key2 result: {bytes_to_hex(encrypted2)}")
    print(f"Different: {'Yes' if encrypted1 != encrypted2 else 'No'}")

if __name__ == "__main__":
    main()