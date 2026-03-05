from cryptography.fernet import Fernet


KEY = Fernet.generate_key()

cipher = Fernet(KEY)


def encrypt_data(data):

    return cipher.encrypt(

        data.encode()

    ).decode()


def decrypt_data(data):

    return cipher.decrypt(

        data.encode()

    ).decode()
