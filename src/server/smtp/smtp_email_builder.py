from __future__ import annotations
from typing import Optional, Union, TypeAlias, Sequence
from dataclasses import dataclass
from .smtp_email import SMTPEmail

OptionalString: TypeAlias = Optional[str]
PortType: TypeAlias = Union[str, int]


@dataclass
class SMTPEmailBuilder:
    host: str = ""
    port: PortType = 0
    username: OptionalString = None
    password: OptionalString = None
    tls: bool = False
    ssl: bool = False

    def set_host(self, host: str) -> SMTPEmailBuilder:
        self.host = host

        return self

    def set_port(self, port: PortType) -> SMTPEmailBuilder:
        self.port = port

        return self

    def set_credentials(self, username: str, password: str) -> SMTPEmailBuilder:
        self.username = username
        self.password = password

        return self

    def set_ssl(self, ssl: bool) -> SMTPEmailBuilder:
        self.ssl = ssl

        return self

    def set_tls(self, tls: bool) -> SMTPEmailBuilder:
        self.tls = tls

        return self

    def build(self) -> SMTPEmail:
        credentials: Optional[Sequence[str]] = None

        if self.username and self.password:
            credentials = self.username, self.password

        return SMTPEmail(self.host, int(self.port), credentials, self.ssl, self.tls)
