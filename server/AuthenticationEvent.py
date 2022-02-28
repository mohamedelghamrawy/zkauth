from dataclasses import dataclass
from _datetime import datetime


@dataclass
class AuthenticationEvent:
    """Class for keeping track of authentication events"""
    time = datetime.now()
    t: int
    c: int
