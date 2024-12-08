from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from typing import Literal, NoReturn, Self

class Secret:
    def __init__(
        self: Self,
        key: str
    ) -> NoReturn:
        self.__fernet = Fernet(key)
        self.__pw = PasswordHasher(
            encoding='utf-8'
        )

    def encrypt(
        self: Self,
        data: str
    ) -> str:
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
        return self.__fernet.decrypt(
            token
        ).decode(
            encoding='utf-8'
        )

    def hash(
        self: Self,
        password: str
    ) -> str:
        return self.__pw.hash(
            password
        )

    def verify(
        self: Self,
        hash: str,
        password: str
    ) -> Literal[True]:
        return self.__pw.verify(
            hash, password
        )

    @classmethod
    @property
    def new(
        self: Self
    ) -> str:
        """
            Generate cryptographic key.
        """
        return Fernet.generate_key().decode(
            encoding='utf-8'
        )
