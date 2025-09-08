import pytest
from src.lightcrypt import LightCrypt


def test_encrypt_decrypt():
    """Test basic encryption and decryption"""
    key = b"TestKey123456789"
    cipher = LightCrypt(key)

    message = b"Do I like cats, or do I like dogs?"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    assert message == decrypted


def test_different_messages():
    """Test that different messages give different ciphertext"""
    key = b"TestKey123456789"
    cipher = LightCrypt(key)

    msg1 = b"Message one"
    msg2 = b"Message two"

    enc1 = cipher.encrypt(msg1)
    enc2 = cipher.encrypt(msg2)

    assert enc1 != enc2


def test_wrong_key():
    """Test that wrong key gives wrong result or raises error"""
    msg = b"Secret message"

    key1 = b"CorrectKey123456"
    key2 = b"WrongKey12345678"

    cipher1 = LightCrypt(key1)
    cipher2 = LightCrypt(key2)

    encrypted = cipher1.encrypt(msg)

    with pytest.raises(AssertionError) as e:
        decrypted = cipher2.decrypt(encrypted)
        assert decrypted == msg

def test_empty_message():
    """Test encryption and decryption of an empty message"""
    key = b"TestKey123456789"
    cipher = LightCrypt(key)

    msg = b""
    encrypted = cipher.encrypt(msg)
    decrypted = cipher.decrypt(encrypted)

    assert decrypted == msg