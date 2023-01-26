from start import app

from api.controllers.drive_controller import DriveController
from api.controllers.user_auth_controller import UserAuthController


app.http.add_resource(DriveController, "/drive")
app.http.add_resource(UserAuthController, "/user/auth")
