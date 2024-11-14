from dataclasses import dataclass


@dataclass
class UserInfo:
    first_name: str = "John"
    last_name: str = "Doe"
    postal_code: str = "12345"
