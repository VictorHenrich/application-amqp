from typing import Mapping
from pathlib import Path


__PATH_DRIVES__: Path = Path.cwd() / "drives" / "users"

__MIME_TYPES__: Mapping[str, str] = {
    "bin": "application/octet-stream",
    "txt": "text/plain",
    "pdf": "application/pdf",
    "html": "plain/html",
    "bz": "application/x-bzip",
    "css": "text/css",
    "jpg": "image/jpeg",
    "csv": "text/csv",
    "doc": "application/msword",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "gz": "application/gzip",
    "gif": "image/gif",
    "ico": "image/vnd.microsoft.icon",
    "jar": "application/java-archive",
    "jpeg": "mage/jpeg",
    "js": "text/javascript",
    "mp3": "audio/mpeg",
    "mp4": "video/mp4",
    "odp": "application/vnd.oasis.opendocument.presentation",
    "ods": "application/vnd.oasis.opendocument.spreadsheet",
    "odt": "application/vnd.oasis.opendocument.text",
    "oga": "audio/ogg",
    "ogv": "video/ogg",
    "ogx": "application/ogg",
    "png": "image/png",
    "php": "application/x-httpd-php",
    "rar": "application/vnd.rar",
    "svg": "image/svg+xml",
    "tar": "application/x-tar",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "xml": "application/xml",
    "zip": "application/zip",
    "7z": "application/x-7z-compressed",
}
