class DriveNotFoundError(BaseException):
    def __init__(self) -> None:
        super().__init__("Drive not found!")
