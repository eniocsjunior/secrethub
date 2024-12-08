from typing import Literal
from secrethub import Secret

def test_generate_new_cryptographic_key() -> Literal[True]:
    assert isinstance(Secret.new, str)

def test_encrypt_message(secret: Secret, message: str) -> Literal[True]:
    assert secret.decrypt(secret.encrypt(message)) == message

def test_hash_message(secret: Secret, message: str) -> Literal[True]:
    assert secret.verify(secret.hash(message), message)
