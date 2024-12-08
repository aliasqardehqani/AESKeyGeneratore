from django.http import JsonResponse
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os
from cryptography.hazmat.primitives import serialization

def transfer_key(request):
    with open("rsa_keys/public_key.pem", "rb") as public_file:
        public_key = serialization.load_pem_public_key(public_file.read())

    aes_key = os.urandom(32)  # 256-bit key

    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return JsonResponse({"encrypted_key": encrypted_aes_key.hex()})
