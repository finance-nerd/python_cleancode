from datetime import datetime
from dataclasses import dataclass


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "** 민감한 정보**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%m")
        }


@dataclass
class LoginEvent:
    SERIALIZER = LoginEventSerializer

    username: str
    password: str
    ip: str
    timestamp: datetime

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()


login_event = LoginEvent("phyhton", "cleancode", "http://", datetime.today())
print(login_event.serialize())
