from django.test import TestCase
from utils.security.encrypt_text import decrypt_text, encrypt_text

class JustTest(TestCase):

    def test01_encrypt(self):
        private_message = "hello world"
        cipher_info = encrypt_text(private_message, "i am chulsu")
        decrypted_message = decrypt_text(cipher_info, "i am chulsu")
        self.assertEqual(private_message, decrypted_message)
