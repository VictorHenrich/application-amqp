from typing import TypeAlias, Union, Sequence, Optional, Type
from ssl import create_default_context
from email.message import EmailMessage
from email.mime.text import MIMEText
from smtplib import SMTP, SMTP_SSL

Port: TypeAlias = Union[str, int]
SMTPServer: TypeAlias = Union[SMTP, SMTP_SSL]
Credentials: TypeAlias = Optional[Sequence[str]]


class SMTPEmail:
    def __init__(
        self, host: str, port: Port, credentials: Credentials, ssl: bool, tls: bool
    ) -> None:
        self.__host: str = host
        self.__port: Port = port
        self.__credentials: Credentials = credentials
        self.__ssl: bool = ssl
        self.__tls: bool = tls

        self.__server: Optional[SMTPServer] = None

    def __start(self) -> None:
        if self.__server:
            return

        if self.__ssl and self.__tls:
            self.__server = SMTP_SSL(
                self.__hsot, self.__port, context=create_default_context
            )

        else:
            self.__server = SMTP(self.__host, self.__port)

        if self.__tls and not self.__ssl:
            self.__server.starttls()

        if self.__credentials:
            username, password = list(self.__credentials)

            self.__server.login(username, password)

    def __finish(self) -> None:
        if self.__server:
            self.__server.close()

            self.__server = None

    def __enter__(self) -> SMTPServer:
        self.__start()

        return self.__server

    def __exit__(
        self, type_error: Type[BaseException], error: BaseException, traceback: str
    ) -> None:
        self.__finish()

    def send(self, from_: str, to: Sequence[str], title: str, content: str) -> None:
        message: EmailMessage = EmailMessage()

        message["Subject"] = title

        message["From"] = from_

        message["To"] = ",".join(to)

        message.attach(MIMEText(content, "html"))

        self.__server.sendmail(message)
