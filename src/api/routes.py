from start import app

from api.controllers.drive_upload_controller import DriveUploadController
from api.controllers.drive_download_controller import DriveDownloadController
from api.controllers.user_auth_controller import UserAuthController


app.http.add_resource(DriveUploadController.DriveUploadMany, "/drive/upload/many")
app.http.add_resource(DriveUploadController.DriveUploadOne, "/drive/upload/one")
app.http.add_resource(DriveDownloadController.DriveDownloadMany, "/drive/download/many")
app.http.add_resource(DriveDownloadController.DriveDownloadOne, "/drive/download/one/<uuid:drive_hash>")
app.http.add_resource(UserAuthController, "/user/auth")
