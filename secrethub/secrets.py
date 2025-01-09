from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from typing import Literal, NoReturn, Self

class Secret:
    """
        To instantiate a Secret class you must first have a key:

        >>> from secrethub import Secret
        >>> new_key = Secret.new
        >>> new_secret
        'UEGVN46SwIOyQCneO-sudqDRlqbM3Td8ygozeoWqY2A='
        >>> secret = Secret(key=new_key)

        Now you can encrypt and decrypt messages:

        >>> message = 'Hello Secret'
        >>> encrypted_message = secret.encrypt(message)
        >>> encrypted_message
        'gAAAAABnVgxFcin82sXSGvZH5Uwia4KDewcK3xk5Kbwiv2Uk95GLXwj0pVxReoQi04M9SJZ6yiYxGp8e6o8j9k0DiBWdEZWOLg=='
        >>> secret.decrypt(encrypted_message)
        'Hello Secret'

        You can also hash passwords and verify them:

        >>> password = '57r0n6p4$5W0rD4n07h1n6'
        >>> hashed_password = secret.hash(password)
        >>> hashed_password
        '$argon2id$v=19$m=65536,t=3,p=4$JB0aad1g1h01VrUK46iv2w$/8Sw0taHXdVi2tBFA4hRaBHPcx8JtJ7Qq71X46TWpP4'
        >>> secret.verify(hashed_password, password)
        True
    """
    def __init__(
        self: Self,
        key: str
    ) -> NoReturn:
        """
            :key: must be 32 url-safe base64-encoded bytes.
        """
        self.__fernet = Fernet(key)
        self.__pw = PasswordHasher(
            encoding='utf-8'
        )

    def encrypt(
        self: Self,
        data: str
    ) -> str:
        """
            Encrypt message.
            Example:

            >>> from secrethub import Secret
            >>> secret = Secret(key=Secret.new)
            >>> message = 'Hello Secret'
            >>> encrypted_message = secret.encrypt(message)
            >>> encrypted_message
            'gAAAAABnVgxFcin82sXSGvZH5Uwia4KDewcK3xk5Kbwiv2Uk95GLXwj0pVxReoQi04M9SJZ6yiYxGp8e6o8j9k0DiBWdEZWOLg=='
        """
        return self.__fernet.encrypt(
            data.encode(
                encoding='utf-8'
            )
        ).decode(
            encoding='utf-8'
        )

    def decrypt(
        self: Self,
        token: str
    ) -> str:
        """
            Decrypt message.
            Example:

            >>> from secrethub import Secret
            >>> secret = Secret(key=Secret.new)
            >>> message = 'Hello Secret'
            >>> encrypted_message = secret.encrypt(message)
            >>> encrypted_message
            'gAAAAABnVgxFcin82sXSGvZH5Uwia4KDewcK3xk5Kbwiv2Uk95GLXwj0pVxReoQi04M9SJZ6yiYxGp8e6o8j9k0DiBWdEZWOLg=='
            >>> secret.decrypt(encrypted_message)
            'Hello Secret'
        """
        return self.__fernet.decrypt(
            token
        ).decode(
            encoding='utf-8'
        )

    def hash(
        self: Self,
        password: str
    ) -> str:
        """
            Hash password.
            Example:

            >>> from secrethub import Secret
            >>> secret = Secret(key=Secret.new)
            >>> password = '57r0n6p4$5W0rD4n07h1n6'
            >>> hashed_password = secret.hash(password)
            >>> hashed_password
            '$argon2id$v=19$m=65536,t=3,p=4$JB0aad1g1h01VrUK46iv2w$/8Sw0taHXdVi2tBFA4hRaBHPcx8JtJ7Qq71X46TWpP4'
        """
        return self.__pw.hash(
            password
        )

    def verify(
        self: Self,
        hash: str,
        password: str
    ) -> Literal[True]:
        """
            Verify hashed password.
            Example:

            >>> from secrethub import Secret
            >>> secret = Secret(key=Secret.new)
            >>> password = '57r0n6p4$5W0rD4n07h1n6'
            >>> hashed_password = secret.hash(password)
            >>> hashed_password
            '$argon2id$v=19$m=65536,t=3,p=4$JB0aad1g1h01VrUK46iv2w$/8Sw0taHXdVi2tBFA4hRaBHPcx8JtJ7Qq71X46TWpP4'
            >>> secret.verify(hashed_password, password)
            True
        """
        return self.__pw.verify(
            hash, password
        )

    @classmethod
    def new(
        self: Self
    ) -> str:
        return Fernet.generate_key().decode(
            encoding='utf-8'
        )
