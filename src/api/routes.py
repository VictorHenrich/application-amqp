from start import app

from api.controllers.drive_upload_controller import DriveUploadController
from api.controllers.drive_download_controller import DriveDownloadController
from api.controllers.user_auth_controller import UserAuthController


app.http.add_resource(DriveUploadController, "/drive/upload")
app.http.add_resource(DriveDownloadController, "/drive/download/<uuid:drive_hash>")
app.http.add_resource(UserAuthController, "/user/auth")
