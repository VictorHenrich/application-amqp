from typing import TypeAlias, Union, Sequence, Optional, Mapping
from ssl import create_default_context
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from smtplib import SMTP, SMTP_SSL


from utils.constants import __MIME_TYPES__

SMTPServer: TypeAlias = Union[SMTP, SMTP_SSL]
Credentials: TypeAlias = Optional[Sequence[str]]
Attachment: TypeAlias = Mapping[str, Union[str, bytes]]


class SMTPEmail:
    def __init__(
        self, host: str, port: int, credentials: Credentials, ssl: bool, tls: bool
    ) -> None:
        self.__host: str = host
        self.__port: int = port
        self.__credentials: Credentials = credentials
        self.__ssl: bool = ssl
        self.__tls: bool = tls

        self.__server: SMTPServer = self.__create_server()

    def __create_server(self) -> SMTPServer:
        if self.__ssl and self.__tls:
            return SMTP_SSL(self.__host, self.__port, context=create_default_context())

        else:
            return SMTP(self.__host, self.__port)

    def __start(self) -> None:
        if self.__tls and not self.__ssl:
            self.__server.starttls()

        if self.__credentials:
            username, password = list(self.__credentials)

            self.__server.login(username, password)

    def send(
        self,
        to: Sequence[str],
        title: str,
        content: str,
        from_: Optional[str] = None,
        attachments: Sequence[Attachment] = None,
    ) -> None:
        self.__start()

        message: EmailMessage = EmailMessage()

        message["Subject"] = title

        message["From"] = from_ or list(self.__credentials)[0]

        message["To"] = ",".join(to)

        message.set_content(content)

        if attachments:
            for attachment in attachments:
                att: MIMEBase = MIMEBase(*(__MIME_TYPES__["stream"].split("/")))

                att.add_header(
                    "Content-Disposition",
                    f'attachment; filename="{attachment["filename"]}"',
                )

                att.set_payload(attachment["content"])

                encode_base64(att)

                message.attach(att)

        self.__server.send_message(message)
