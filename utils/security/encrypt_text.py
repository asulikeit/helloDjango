from Cryptodome.Cipher import AES
import hashlib
from base64 import b64decode, b64encode

from djangoapp.settings import SECRET_KEY

salt = SECRET_KEY[:AES.block_size].encode()

def _get_privatekey(salt_text):
    return hashlib.scrypt(salt_text.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

def encrypt_text(plain_text, salt_text):
    try:
        private_key = _get_privatekey(salt_text)
        cipher_config = AES.new(private_key, AES.MODE_GCM)
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
        cipher_info = {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8'),
        }
        return cipher_info
    except Exception:
        raise Exception("encrypt error")

def decrypt_text(cipher_info, salt_text):
    try:
        cipher_text = b64decode(cipher_info.get('cipher_text'))
        private_key = _get_privatekey(salt_text)
        nonce = b64decode(cipher_info.get('nonce'))
        tag = b64decode(cipher_info.get('tag'))
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode('utf-8')
    except Exception:
        raise Exception("decrypt error")
