from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

users_private_keys = {}


def get_keys(user):
    """Получение пары ключей"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    users_private_keys['user'] = private_key
    pem_priv = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(f"{user}_private.pem", "wb") as f:
        f.write(pem_priv)
    public_key = private_key.public_key()
    pem_pub = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(f"{user}_public.pem", "wb") as f:
        f.write(pem_pub)
    return f'{user}_private.pem'